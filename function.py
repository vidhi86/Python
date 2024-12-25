#content of function is to be indented 4 spaces from the function decalartion
#two line shoulb be left before starting new code after function

def do_something():
    print("I am doing something")


do_something()


#how to change value of global variable form local scope

def change_name():
    global name
    name = "John"

name = "jack"
change_name()
print(name)

# global variable
words = "hello world"
 
 
def hi_world():
    return words
 
 
print(hi_world())