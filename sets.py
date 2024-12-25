
name = { 'john', 'jack', 'rohan', 'yash', 'ruhu','john'}
name2 = {'hari', 'olive','rohan'}

set1 = { 1,2,3,4,5 }
set2 = { 4,5,6,7 }

print(set(range(1,12,2)))            #make a set with start end point and the steps between
print(set(name))                     #make a set
print(list(set(name)))               #convert back to list
name.add('tim')
name.remove('john')
name.discard('raj')                  #will remove the item if present and if not do not throw any error
name.copy()
name.clear()

name.union(name2)   
print(set1 | set2)≥

print(set1.intersection(set2))
print(set1 & set2)

print(set1 - set2)
print(set1.difference(set2))