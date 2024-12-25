#importing a module
import random 

print (random.randint(1,10))          # gives random interger between 1-10


#importing a function from module
from random import randint

print(randint(20,30))


#importing gllobally - imports all the function from that module
from random import *

print(randint(40,90))
