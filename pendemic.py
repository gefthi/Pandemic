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

connections = [
    ("San Francisco", "Tokyo"), ("San Francisco", "Manila"), 
    ("San Francisco", "Los Angeles"), ("San Francisco", "Chicago"),
    ("Chicago", "San Francisco"), ("Chicago", "Los Angeles"),
    ("Chicago", "Mexico City"), ("Chicago", "Atlanta"), 
    ("Chicago", "Montreal"), 
    ("Los Angeles", "Sydney"), ("Los Angeles", "Chicago"), 
    ("Los Angeles", "Mexico City"), ("Los Angeles", "San Francisco"),
    ("Mexico City", "Miami"), ("Mexico City", "Bogota"),
    ("Mexico City", "Lima"), ("Mexico City", "Los Angeles"),
    ("Mexico City", "Chicago"),
    ("Miami", "Washington"), ("Miami", "Bogota"), 
    ("Miami", "Mexico City"), ("Miami", "Atlanta"),
    ("Bogota", "Miami"), ("Bogota", "Mexico City"), 
    ("Bogota", "Lima"), ("Bogota", "Sao Paulo"), ("Bogota", "Buenos Aires"),
    ("Lima", "Mexico City"), ("Lima", "Bogota"), ("Lima", "Santiago"),
    ("Santiago", "Lima"),
    ("Buenos Aires", "Bogota"), ("Buenos Aires", "Sao Paulo"),
    ("Sao Paulo", "Bogota"), ("Sao Paulo", "Buenos Aires"), 
    ("Sao Paulo", "Madrid"), ("Sao Paulo", "Lagos"),
    ("Lagos", "Sao Paulo"), ("Lagos", "Khartoum"), ("Lagos", "Kinshasa"),
    ("Kinshasa", "Lagos"), ("Kinshasa", "Khartoum"), ("Kinshasa", "Johannesburg"),
    ("Khartoum", "Cairo"), ("Khartoum", "Lagos"), ("Khartoum", "Kinshasa"), 
    ("Khartoum", "Johannesburg"),
    ("Johannesburg", "Kinshasa"), ("Johannesburg", "Khartoum"),
    ("Montreal", "Chicago"), ("Montreal", "Washington"), ("Montreal", "New York"),
    ("Washington", "Montreal"), ("Washington", "New York"), 
    ("Washington", "Atlanta"), ("Washington", "Miami"),
    ("New York", "Montreal"), ("New York", "Washington"), 
    ("New York", "London"), ("New York", "Madrid"),
    ("Atlanta", "Chicago"), ("Atlanta", "Washington"), ("Atlanta", "Miami"),
    ("London", "New York"), ("London", "Madrid"), ("London", "Essen"), ("London", "Paris"),
    ("Madrid", "New York"), ("Madrid", "London"), ("Madrid", "Paris"), 
    ("Madrid", "Algiers"), ("Madrid", "Sao Paulo"),
    ("Essen", "London"), ("Essen", "Paris"), ("Essen", "Milan"), ("Essen", "St. Petersburg"),
    ("Paris", "London"), ("Paris", "Essen"), ("Paris", "Milan"), 
    ("Paris", "Algiers"), ("Paris", "Madrid"),
    ("Milan", "Essen"), ("Milan", "Paris"), ("Milan", "Istanbul"),
    ("St. Petersburg", "Essen"), ("St. Petersburg", "Istanbul"), 
    ("St. Petersburg", "Moscow"),
    ("Algiers", "Madrid"), ("Algiers", "Paris"), ("Algiers", "Istanbul"), ("Algiers", "Cairo"),
    ("Istanbul", "Milan"), ("Istanbul", "St. Petersburg"), 
    ("Istanbul", "Moscow"), ("Istanbul", "Algiers"), ("Istanbul", "Cairo"), 
    ("Istanbul", "Baghdad"),
    ("Moscow", "St. Petersburg"), ("Moscow", "Istanbul"), ("Moscow", "Tehran"),
    ("Cairo", "Algiers"), ("Cairo", "Istanbul"), ("Cairo", "Baghdad"), 
    ("Cairo", "Riyadh"), ("Cairo", "Khartoum"),
    ("Baghdad", "Istanbul"), ("Baghdad", "Cairo"), ("Baghdad", "Riyadh"), 
    ("Baghdad", "Karachi"), ("Baghdad", "Tehran"),
    ("Tehran", "Moscow"), ("Tehran", "Baghdad"), ("Tehran", "Karachi"), ("Tehran", "Delhi"),
    ("Karachi", "Baghdad"), ("Karachi", "Tehran"), ("Karachi", "Delhi"), 
    ("Karachi", "Mumbai"), ("Karachi", "Riyadh"),
    ("Delhi", "Tehran"), ("Delhi", "Karachi"), ("Delhi", "Mumbai"), 
    ("Delhi", "Chennai"), ("Delhi", "Kolkata"),
    ("Mumbai", "Karachi"), ("Mumbai", "Delhi"), ("Mumbai", "Chennai"),
    ("Riyadh", "Cairo"), ("Riyadh", "Baghdad"), ("Riyadh", "Karachi"),
    ("Chennai", "Mumbai"), ("Chennai", "Delhi"), ("Chennai", "Kolkata"), 
    ("Chennai", "Bangkok"),     ("Chennai", "Jakarta"), 
    ("Kolkata", "Delhi"), ("Kolkata", "Bangkok"), ("Kolkata", "Hong Kong"),
    ("Bangkok", "Kolkata"), ("Bangkok", "Chennai"), 
    ("Bangkok", "Jakarta"), ("Bangkok", "Ho Chi Minh City"), 
    ("Bangkok", "Hong Kong"),
    ("Jakarta", "Chennai"), ("Jakarta", "Bangkok"), 
    ("Jakarta", "Ho Chi Minh City"), ("Jakarta", "Sydney"),
    ("Ho Chi Minh City", "Bangkok"), ("Ho Chi Minh City", "Jakarta"), 
    ("Ho Chi Minh City", "Manila"), ("Ho Chi Minh City", "Hong Kong"),
    ("Sydney", "Jakarta"), ("Sydney", "Manila"), ("Sydney", "Los Angeles"),
    ("Manila", "Ho Chi Minh City"), ("Manila", "Sydney"), 
    ("Manila", "San Francisco"), ("Manila", "Taipei"), ("Manila", "Hong Kong"),
    ("Hong Kong", "Bangkok"), ("Hong Kong", "Ho Chi Minh City"), 
    ("Hong Kong", "Manila"), ("Hong Kong", "Shanghai"), 
    ("Hong Kong", "Taipei"), ("Hong Kong", "Kolkata"),
    ("Taipei", "Manila"), ("Taipei", "Hong Kong"), ("Taipei", "Shanghai"), ("Taipei", "Osaka"),
    ("Shanghai", "Beijing"), ("Shanghai", "Hong Kong"), 
    ("Shanghai", "Taipei"), ("Shanghai", "Seoul"), ("Shanghai", "Tokyo"),
    ("Beijing", "Shanghai"), ("Beijing", "Seoul"),
    ("Seoul", "Beijing"), ("Seoul", "Shanghai"), ("Seoul", "Tokyo"),
    ("Tokyo", "Seoul"), ("Tokyo", "Shanghai"), ("Tokyo", "Osaka"), 
    ("Tokyo", "San Francisco"),
    ("Osaka", "Tokyo"), ("Osaka", "Taipei")
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

    for city1, city2 in connections:
        cities[city1].add_connection(cities[city2])

    """
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
