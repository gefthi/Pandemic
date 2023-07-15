
class City:
    pass

class Board:
    def __init__(self) -> None:
        pass

    def setup(self):
        pass

class City:
    def __init__(self, name:str) -> None:
        self.name=name
        self.connected_cities=[]     
        
    def __str__(self) -> str:
        return self.name
    
    def connectCity(self,city: City):
        self.connected_cities.append(city)
        city.connected_cities.append(self)

class Game:

    board=Board()

    def __init__(self) -> None:
        pass


chicago=City("Chicago")
newyork=City("New York")
sanfr=City("San Francisco")

chicago.connectCity(newyork)
chicago.connectCity(sanfr)

print(*chicago.connected_cities)
print(*newyork.connected_cities)
print(*sanfr.connected_cities)
