##1 - variable assignment
num = 12
dec_value = 34.55875860868
is_decimal = True
string = "45678"
num = 17
string2 = "Vidhi Sharma"


##2 - operations

sum = 34 + 5
diff = 34 - 5
div = 15 / 3
prod =  3 * 4
expon = 3 ** 8
floor_div = 10 // 3
mod = 17 % 5

##3 - basic functions
## () >> ** >> %,/,//,* >> +,-
round(dec_value, 2)             #rounded up to 2 decimal place
type(expon)                     #type of variable
print('this\tis\tbag')          #for horizontal gap
print('this\nis\nbag')          #for vertical gap
print('this\\is\\bag')          #for escape sequence
print("this \'is\' bag")        #for qouting within line
int(string)                     #convert into intrger
float(string)                   #to float
str(num)                        #to string
bool(num)                       #tell if its a truthy or falsy value
abs(-5)                         #absolute value
max(1, 2, 3, 4, 5)              #max valu
string2.lower()                 #make all in lower case
string2.upper()                 #make all in upper case
string2.capitalize()            #capitalize first letter
string2.islower()               #tell if all are lower or not
string2.isupper()               #tell if all are upper or not
string2.isalpha()               #tell if all are alphabets or not
string2.isdigit()               #tell if all are digits or not
string2.isalnum()               #tell if all are alphanumeric or not
string2.replace('Vidhi', 'Vidh') #replace 'Vidhi'
string2.split(' ')              #split string with space
string2.strip()                 #remove leading and trailing spaces
string2.rstrip(" Sharma")                #remove spaces or characters from right side
string2.lstrip("Vidhi ")                #from left side
string2.startswith('Vidhi')     #tell if string starts with 'Vidhi'
string2.endswith('Sharma')      #tell if string ends with 'Sharma'
string2.count('Vidhi')          #count 'Vidhi' in string
string2.find('Vidhi')           #find index of 'Vidhi'
string2.rfind('Vidhi')          #find index of 'Vidhi' from
string2.index('Vidhi')          #find index of 'Vidhi'
string2.rindex('Vidhi')         #find index of 'Vidhi' from
string2.center(20)              #center string in 20 spaces
string2.ljust(20,"-")           #left justify string in 20 spaces filled with hyohen
string2.rjust(20)               #right justify string in 20 spaces
string2.zfill(20)               #zero fill string in 20 spaces
string2.join()                  #join string with no space
string2.join(' ')               #join string with space
string2.join('-')               #join string with '-'
len(string)                     #get length
format()
list(string2)                   #converts string into list
tuple(string2)                  #converts string into tuple
num is string2                  #use to check if are equal                              

##4 - activity
Penne = 16.68
Arrabiata = 6.98
Garlic = 16.78
Seasoning = 15.26
Baguettes = 3.00
Meatballs = 4.39

sum_total = Penne + Arrabiata + Garlic + Seasoning + Baguettes + Meatballs
print(round(sum_total,2))

##5 - function 

#content of function is to be indented 4 spaces from the function decalartion
#two line shoulb be left before starting new code after function

def do_something():
    print("I am doing something")


do_something()

##6 - if statements

if num == 12:
    print("num is 12")
elif num == 17:
    print('num is 17')
else: 
    print("num is not 12 or 17")