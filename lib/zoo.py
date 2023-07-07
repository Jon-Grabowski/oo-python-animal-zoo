from lib.animal import Animal

class Zoo:

    all = []
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.all.append(self)
    

#TODO Left off at *Zoo#animal_species from README 
    
