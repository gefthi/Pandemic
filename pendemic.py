import random

city_data = [
    ("San Francisco", "blue"), ("Chicago", "blue"), ("Montreal", "blue"),
    ("New York", "blue"), ("Washington", "blue"), ("London", "blue"),
    ("Madrid", "blue"), ("Paris", "blue"), ("Essen", "blue"), ("Milan", "blue"),
    ("St. Petersburg", "blue"), ("Atlanta", "blue"), 
    ("Los Angeles", "yellow"), ("Mexico City", "yellow"), ("Miami", "yellow"),
    ("Bogota", "yellow"), ("Lima", "yellow"), ("Santiago", "yellow"),
    ("Buenos Aires", "yellow"), ("Sao Paulo", "yellow"), ("Lagos", "yellow"),
    ("Khartoum", "yellow"), ("Johannesburg", "yellow"), ("Kinshasa", "yellow"),
    ("Algiers", "black"), ("Istanbul", "black"), ("Moscow", "black"),
    ("Tehran", "black"), ("Baghdad", "black"), ("Riyadh", "black"),
    ("Karachi", "black"), ("Delhi", "black"), ("Mumbai", "black"),
    ("Chennai", "black"), ("Kolkata", "black"), ("Beijing", "red"),
    ("Seoul", "red"), ("Tokyo", "red"), ("Shanghai", "red"), 
    ("Hong Kong", "red"), ("Taipei", "red"), ("Osaka", "red"), 
    ("Bangkok", "red"), ("Manila", "red"), ("Ho Chi Minh City", "red"), 
    ("Jakarta", "red"), ("Sydney", "red")
]

class Card:
    def __init__(self, name):
        self.name = name

class City:
    def __init__(self, name, color):
        self.name = name
        self.color = color        
        self.disease_cubes = { 'blue': 0, 'yellow': 0, 'black': 0, 'red': 0 }
        self.research_station = False
        self.connections = []

    def add_connection(self, city):
        self.connections.append(city)

class Player:
    def __init__(self):
        self.location = None
        self.hand = []
        self.role = ""

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, Card):
        self.cards.append(Card)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

class Game:
    def __init__(self, cities, player_deck, infection_deck):
        self.cities = cities
        self.players = [Player() for _ in range(4)]  # Assuming 4 players
        self.player_deck = player_deck
        self.infection_deck = infection_deck
        """self.outbreaks = 0
        self.disease_cubes = { 'blue': 24, 'yellow': 24, 'black': 24, 'red': 24 }
        self.cures = { 'blue': False, 'yellow': False, 'black': False, 'red': False }
        self.player_deck = []  # needs to be filled with cards
        self.infection_deck = []  # needs to be filled with cards
        """

def setup():
    # Set up cities and connections
    cities = {}
    for city_name, color in city_data:
        cities[city_name] = City(city_name, color)

    """for city1, city2 in connections:
        cities[city1].add_connection(cities[city2])

    # Create player deck
    player_deck = Deck()
    for city in cities.values():
        player_deck.add_card(Card(city.name))

    # Create infection deck
    infection_deck = Deck()
    for city in cities.values():
        infection_deck.add_card(Card(city.name))

    # Create game
    game = Game(cities, player_deck, infection_deck)

    # Shuffle player deck and deal initial hands
    game.player_deck.shuffle()
    for player in game.players:
        for _ in range(2):
            card = game.player_deck.draw_card()
            player.hand.append(card)

    # Initial infection phase
    for _ in range(3):
        card = game.infection_deck.draw_card()
        game.cities[card.name].disease_cubes += 3
    for _ in range(3):
        card = game.infection_deck.draw_card()
        game.cities[card.name].disease_cubes += 2
    for _ in range(3):
        card = game.infection_deck.draw_card()
        game.cities[card.name].disease_cubes += 1
     # Randomly choose player roles and place players in Atlanta
    roles = ["Medic", "Scientist", "Researcher", "Quarantine Specialist", "Dispatcher"]
    for player in game.players:
        player.role = random.choice(roles)
        roles.remove(player.role)
        player.location = game.cities["Atlanta"]
"""
    return game

deck=Deck()
card=Card
deck.add_card(card)
print(deck.draw_card())
