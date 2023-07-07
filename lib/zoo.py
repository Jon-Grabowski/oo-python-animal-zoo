from typing import Any
from lib.animal import Animal

class Zoo:

    all = []
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.all.append(self)

    def __repr__(self):
        return f"<Name: {self.name}, Location: {self.location}>"

    def get_name(self):
        return self._name  
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Name must be a string.")
    name = property(get_name, set_name)

    def get_loc(self):
        return self._location   
    def set_loc(self, location):
        if isinstance(location, str):
            self._location = location
        else:
            print("Location must be a string.")
    location = property(get_loc, set_loc)

    def animals(self):
        return [animal for animal in Animal.all if animal.zoo == self]

    def animal_species(self):
        species_in_zoo = []
        for animal in Animal.all:
            if animal.zoo == self and animal.species.capitalize() not in species_in_zoo:
                species_in_zoo.append(animal.species)
        return species_in_zoo
    
    def find_by_species(self, species):
        species_list = []
        for animal in Animal.all:
            if animal.zoo == self and animal.species.lower() == species.lower():
                species_list.append(animal)
        return species_list
    
    def animal_nicknames(self):
        return [animal.nickname for animal in Animal.all if animal.zoo == self]

    def find_by_location(location):
        return [zoo.name for zoo in Zoo.all if zoo._location == location]
        