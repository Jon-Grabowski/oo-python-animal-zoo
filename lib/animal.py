import ipdb

class Animal:
    all = []
    species_switch = 0
    nickname_switch = 0
    
    def __init__(self, species, weight, nickname, zoo):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo = zoo
        Animal.all.append(self)

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

#TODO Left off at *Animal.find_by_species from README 

a1 = Animal( 'Lion', 75, 'Luke', 'zoo' )
a2 = Animal( 'Cat', 7, 'Potato', 'zoo2' )
print(a1.zoo)
# a1.nickname = "pig"
# print(a1.nickname)