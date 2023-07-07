from lib.animal import Animal
from lib.zoo import Zoo

# code here


# e.g.  

z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
z2 = Zoo( 'Happy Zoo', 'Bodi, CA' )
z3 = Zoo( 'Sad Zoo', 'Godi, CA' )
z4 = Zoo( 'Meh Zoo', 'Lodi, CA' )
a1 = Animal( 'Lion', 75, 'Luke', z1 )
a2 = Animal( 'Cat', 7, 'Potato', z2 )
a3 = Animal( 'Cat', 4, 'Basil', z2 )
a4 = Animal( 'tiger', 17, 'Frank', z1 )
a5 = Animal( 'monkey', 6, 'Dunstin', z2 )






# ipdb allows us to stop our code & test stuff
import ipdb; ipdb.set_trace()
print( 'Thanks for visiting the zoo!' )