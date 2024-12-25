t1 = (1,2,3,4,5,6,7,8)

print(tuple(['abc','def','xyz']))
print(tuple('abcd'))
print(tuple({"a":1,"b":2,"c":3}))
print(tuple([1,2,3]))

#slicing can be done same as list
print(t1[::3])              #gives all the numbers with difference of 3
print(t1[1::2])             #even only
print(t1[7::-1])            #in reverse
#iteration can also be done in same way
print(t1.__sizeof__())            #tells the size of tuple
print(t1.count(2))               #returns the times 2 is repeated in tuple