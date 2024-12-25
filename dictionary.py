animals = {
    1: 'elephant',
    2: 'camel',
    3: 'rabbit',
    4: 'tiger',
    5: 'deer'
}

print(animals[1])                 
print(3 in animals)                    
print(6 not in animals)
print('deer' in animals.values())
print('rat' not in animals.values())
print(len(animals))

print(animals.keys())                      #gives all the keys
for key in animals.keys():
    print(key)                             #prints all the keys



print(animals.values())                      #gives all the values
for values in animals.values():
    print(values)                             #prints all the values


print(animals.items())                         #return tuples in key value form
for key, value in animals.items():
    print(key,value)                           #gives key and value


print(animals.get( 3, "3 is not there"))      #this will take 2 agruments first the key

animals.pop(4)                               #pops out the key value pair with the specified key and return the value
animals.popitem()                              #pops last key value pair
animals.clear()                                #clear
animals.update({6:'lion',7:'tiger'})           #add new key value pair
animals[8] = 'leopard'
animals.setdefault(9, 'horse')                 #set a default value for this key and would not be overwritten 
animals.copy()                                 #make a copy with different reference




info = {}.fromkeys("abc", "all are same")           #first argument is taken as a list and second as the 
                                                    #value for all of them
print(info)
details = {}.fromkeys(['john', 'jack'], [34,56])
print(details)



age = dict(jack=34, roo=56)                        #with dict funtion you cannot use key starting with 
                                                   #number or any special characters
print(age)