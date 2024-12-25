name = ['john', 'reeta', 'jack', 'mark']
number = [1,2,3,4,5,6,7,8,9]
print(list(name[0]))


#in or not in
print('john' in name)
print('jack' not in name)


# slicing
print(number[:4])               #will give all the value starting from index 0 to toh index less than 4
print(number[2:7])              #will give value between 2 and index one less than 7
print(number[5:])               #will give all the numbers persent at and after 6th index


#reassigning

name[2] = 'rohan'
number[2:4] = [10,11]
print(name)
print(number)

#methods
del name[1]                     
name.remove('john')              #if we remove an item that appears multiple time in the list it will just remove the 
                                 # first item from the list

name.append('leo')               #adds item to the end of list
name.insert(3, 'priya')          #insert anywhere in list
name.sort()                      #sort in asc
name.sort(reverse=True)          #sort in desc (sorting is done in ASCIIbetical order)
name.sort(key=str.lower)         #this sort all in alphabetical order with either lower or upper case initials
name.index('leo')                #find index of item (in case of multiple items only index of foirst one is returned)
name.pop()                       #removes and return the last value
print(name.__sizeof__())   
print(name)

#reference
list1 = [1,2,3,4,5]
list2 = list1                   # this happens due to the same refference thought the assignments are diffirent 
list2[2] = 6                    # helpful in saving memory space
print(list1)
print(list2)

import copy
list3 = copy.deepcopy(list1)      #this is used to create a copy of list with totally new reference
list3[2] = 7                      #this will only change list 2 

