import ipdb

class Animal:
    all = []
    species_switch = 0
    nickname_switch = 0
    
    def __init__(self, species, weight, nickname, zoo):
        self.species = species.capitalize()
        self.weight = weight
        self.nickname = nickname
        self.zoo = zoo
        Animal.all.append(self)

    def __repr__(self):
        return f"<Name: {self.nickname}, Species: {self.species}>"

    def get_spec(self):
        return self._species   
    def set_spec(self, species):
        if self.species_switch == 0:
            self._species = species
            self.species_switch += 1
        else:
            print("Species type can not change")
    species = property(get_spec, set_spec)

    def get_nick(self):
        return self._nickname   
    def set_nick(self, nickname):
        if self.nickname_switch == 0:
            self._nickname = nickname
            self.nickname_switch += 1
        else:
            print("Nickname can not change")
    nickname = property(get_nick, set_nick)




    def find_by_species(species):
        species_list = [animal for animal in Animal.all if animal.species.lower() == species.lower()]
        if len(species_list) > 0:
            print(f'There are {len(species_list)} animals of that species.')
            return species_list
        else:
            print('No animals of that species, try looking for a different one!')
