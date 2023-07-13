import random
from city import City,Disease 
from player import Player,Medic,Dispatcher,Researcher


class Game:
    def __init__(self, cities, diseases, players):
        self.cities = cities
        self.diseases = diseases
        self.players = players
        self.player_deck = self.create_player_deck(6)
        self.infection_deck = self.create_infection_deck()
        self.infection_discard = []
        self.outbreaks = 0
        self.infection_rate = 2
        self.disease_cubes = {disease: 24 for disease in diseases}
        self.one_quiet_night = False

    def create_player_deck(self,epidemics):
        # Partition the deck into roughly equal piles and shuffle an epidemic card into each.
        city_cards = [city.name for city in self.cities]
        random.shuffle(city_cards)
        piles = self.partition_deck(city_cards, epidemics)  # Create N piles for N epidemic cards.
        for pile in piles:
            pile.append("Epidemic")
            random.shuffle(pile)
        deck = [card for pile in piles for card in pile]  # Flatten the piles into a single deck.
        return deck

    def create_infection_deck(self):
        # The infection deck contains only city cards.
        #deck = [city.name for city in self.cities]
        #random.shuffle(deck)
        #return deck
        deck = self.cities.copy()
        random.shuffle(deck)
        return deck
    
    def draw_card(self, player):
        card = self.player_deck.pop()
        if card == "Epidemic":
            self.epidemic()
        else:
            player.draw_card(card)

    def epidemic(self):
        # Increase the outbreak rate, infect cities, and intensify by shuffling the player deck.
        self.outbreaks += 1
        self.infection_rate = min(self.infection_rate + 1, 4)
        self.intensify()

    def intensify(self):
        random.shuffle(self.infection_discard)
        self.infection_deck = self.infection_discard + self.infection_deck
        self.infection_discard = []

#setup should not infect with random deseases!
    def setup(self):
        # At the beginning of the game, infect some cities with each disease.
        for disease in self.diseases:
            cities = random.sample(self.cities, 3)
            for city in cities:
                city.infect(disease, random.randint(1, 3))

    def turn(self, player):
        # At the beginning of each player's turn, draw two cards.
        for _ in range(2):
            if self.player_deck:
                self.draw_card(player)
            else:
                print("The player deck is empty. The players have lost!")
                return

        # The player can perform actions here...

        # After the player's actions, infect cities based on the current infection rate.
        if not self.one_quiet_night:
            self.infect_cities()
        else:
            self.one_quiet_night = False

    def play_one_quiet_night(self):
        self.one_quiet_night = True

    def infect_cities(self):
       # Infect cities based on the top cards of the infection deck.
        for _ in range(self.infection_rate):
            if self.infection_deck:
                city = self.infection_deck.pop()
                disease = random.choice(self.diseases)  # Choose a random disease for simplicity.
                city.infect(disease)
                self.infection_discard.append(city)
            else:
                print("The infection deck is empty. The players have lost!")
                return

    def run(self):
        self.setup()
        while True:
            for player in self.players:
                print(f"--- {player.role}'s turn in {player.city.name} ---")
                self.turn(player)
                if self.check_loss():
                    print("The players have lost!")
                    return
                if self.check_win():
                    print("The players have won!")
                    return

    def check_win(self):
        # The players win if all diseases are cured.
        return all(disease.cured for disease in self.diseases)

    def check_loss(self):
        # The players lose if there are 8 or more outbreaks or the player deck is empty.
        return self.outbreaks >= 8 or not self.player_deck or any(cubes == 0 for cubes in self.disease_cubes.values())
    
    @staticmethod
    def partition_deck(deck, num_partitions):
        avg = len(deck) // num_partitions
        remainder = len(deck) % num_partitions
        return [deck[i * avg + min(i, remainder):(i + 1) * avg + min(i + 1, remainder)] for i in range(num_partitions)]


