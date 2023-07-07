from lib.animal import Animal
from lib.zoo import Zoo

# code here


# e.g.  

z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
z2 = Zoo( 'Happy Zoo', 'Bodi, CA' )
z3 = Zoo( 'Sad Zoo', 'Godi, CA' )
z4 = Zoo( 'Meh Zoo', 'Podi, CA' )
a1 = Animal( 'Lion', 75, 'Luke', z1 )
print(a1.species)
a1.species = 'Pig'
print(a1.species)






# ipdb allows us to stop our code & test stuff
import ipdb; ipdb.set_trace()
print( 'Thanks for visiting the zoo!' )