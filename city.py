import random

class Disease:
    def __init__(self, name,color):
        self.name = name
        self.color = color
        self.outbreak_chance = 0.1
        self.cured = False

    def cure(self):
        self.cured = True


class City:
    def __init__(self, name,color):
        self.name = name
        self.color = color
        self.diseases = {}
        self.connected_cities = []
        self.research_station = False

    def add_disease(self, disease, infection_level=0):
        self.diseases[disease] = infection_level

    def connect(self, city):
        self.connected_cities.append(city)
        city.connected_cities.append(self)

    def infect(self, disease, infection_level=1,outbreak_from=None):
        if game.disease_cubes[disease] == 0:
            print(f"No more {disease.name} cubes left. The players have lost!")
            return
        if disease not in self.diseases:
            self.add_disease(disease)
        self.diseases[disease] += infection_level
        if self.diseases[disease] > 3:
            self.outbreak(disease,outbreak_from)

    def outbreak(self, disease, outbreak_from):
        print(f"Outbreak in {self.name}!")
        for city in self.connected_cities:
            if city != outbreak_from:
                city.infect(disease, outbreak_from=self)
        
    def treat(self, disease, treatment_level=1):
        assert disease in self.diseases, "Disease not present in this city."
        self.diseases[disease] = max(0, self.diseases[disease] - treatment_level)

    def build_research_station(self):
        self.research_station = True

