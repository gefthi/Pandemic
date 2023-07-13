class Player:
    def __init__(self, city, game) #role=None):
        self.city = city
        #self.role = role
        self.game=game

    def draw_card(self, card):
        self.hand.append(card)
        if len(self.hand) > 7:  # hand limit
            self.discard_card()

    def discard_card(self):
        # For simplicity, discard a random card.
        self.hand.pop(random.randint(0, len(self.hand) - 1))

    def charter_flight(self, city):
        assert self.city.name in self.hand, "Must discard the card that matches the current city."
        self.hand.remove(self.city.name)
        self.city = city

    def shuttle_flight(self, city):
        assert self.city.research_station, "Must be in a city with a research station."
        assert city.research_station, "Must move to a city with a research station."
        self.city = city

    def share_knowledge(self, other_player, card):
        assert card in self.hand or card in other_player.hand, "Card not in hand."
        assert self.city == other_player.city, "Both players must be in the same city."
        if card in self.hand:
            self.hand.remove(card)
            other_player.hand.append(card)
        else:
            other_player.hand.remove(card)
            self.hand.append(card)

    def move(self, city):
        assert city in self.city.connected_cities, "Can only move to a connected city!"
        self.city = city

    def direct_flight(self, card):
        assert card in self.hand, "Card not in hand."
        for city in self.cities:
            if city.name == card:
                self.move(city)
                self.hand.remove(card)
                break

    def treat(self, disease):
        if self.role == "Medic":
            self.city.treat(disease, self.city.diseases[disease])
        else:
            self.city.treat(disease)

    def build_research_station(self):
        self.city.build_research_station()

    def play_one_quiet_night(self):
        assert "One Quiet Night" in self.hand, "One Quiet Night card not in hand."
        self.hand.remove("One Quiet Night")
        self.game.play_one_quiet_night()

    def cure(self, disease):
        #if self.role == "Scientist":
        #    self.city.build_research_station()
        if self.city.research_station and self.hand.count(disease.color) >= 5:
            disease.cure()
            print(f"{disease.name} has been cured!")
            # Remove 5 cards of the disease's color from the player's hand.
            for _ in range(5):
                self.hand.remove(disease.color)

    def play_event_card(self, card):
        assert card in self.hand, "Card not in hand."
        if card == "Government Grant":
            # Build a research station in any city.
# ??? self.cities is not there            
            city = random.choice(self.cities)  # Choose a random city for simplicity.
            city.build_research_station()
        elif card == "Airlift":
            # Move any player to any city.
            player = random.choice(self.players)  # Choose a random player for simplicity.
            city = random.choice(self.cities)  # Choose a random city for simplicity.
            player.move(city)
        # ... other event cards ...

        self.hand.remove(card)

class Dispatcher(Player):
    def move(self, player, city):
        assert city in player.city.connected_cities or city in self.city.connected_cities, \
            "Can only move to a connected city or a city connected to the Dispatcher's city!"
        player.city = city


class Researcher(Player):
    def share_knowledge(self, other_player, card):
        assert card in self.hand, "Card not in hand."
        self.hand.remove(card)
        other_player.hand.append(card)

class Medic(Player):
    def treat(self, disease):
        # Remove all cubes of the disease from the city.
        self.city.diseases[disease] = 0
        print(f"All {disease.name} cubes have been removed from {self.city.name} by the Medic.")

    def move(self, city):
        super().move(city)
        # Automatically treat cured diseases in the city.
        for disease in self.city.diseases.keys():
            if disease.cured:
                self.treat(disease)
