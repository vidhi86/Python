
#while loop
count = 0

while count < 4:
    print("Hello, World!")
    count += 1


#for loop

arr = [1,2,3,4,5,6,7,8,9]
for i in arr:
    print(i)



#range
## with one argument it start from 1 till the number 
numbers = range(10)
for i in numbers:
    print(i)          


## with two arguments it define the range between which number to be printed
numbers = range(1, 10)
for i in numbers:
    print(i)

## with three argumenrts it defines the range between two number and different between each 
numbers = range(1, 10, 2)
for i in numbers:
    print(i)

numbers = range(20, 10, -4)
for i in numbers:
    print(i)