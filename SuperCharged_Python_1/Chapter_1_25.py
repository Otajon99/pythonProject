# List
def my_func():
    return [10,20,5]
print(my_func())



# Tuple
def my_func():
    return 10,20,5
print(my_func())


# Global Variables

def my_func():
    global foo      # Calling Global variable inside of Function
    foo=5
    print(foo)
my_func()



foo=18               # Global variables
def my_func():
    print(foo)
my_func()