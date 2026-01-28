#Functions
#A function is a block of code that performs a specific task.Functions help in organizing code, reusing code, and improving readability.

## syntax
from ast import Expression


def function_name(parameters):
    """Docstring"""
    # Function body
    return Expression

## why functions?
num=24
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

#Program through Function bcz it reduce redundancy
def even_or_odd(num):
    """This function finds even or odd"""
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")

even_or_odd(24)

#Function with multiple parameters
def add(a,b):
    c=a+b
    return c
result=add(3,5)
print(result)

#Default Parameters
def greet(name="Anuj"):
    print(f"Hello {name}, Welcome to paradise")

#Call the functions
greet()

#Variable length arguments

#Positional and Keywords Arguments
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(3,4,5,6,6,7,8,8) #In postional argument we should always give only value

#Keyword Arguments
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(name="Anuj",age=18,country="India") #In Keyword Argument we should always give key value pair 

#Taking both arguments in one code
def print_information(*args,**kwargs):
    for number in args:
        print(f"Positional Argument ->{number}")
    for key,value in kwargs.items():
        print(f"Keyword Arguments ->{key}:{value}")

print_information(1,2,3,4,True,name="Anuj",age=18,state="delhi") #When giving both keyword argument are always defined after the positional argument

#Return Statement
def addition(a,b):
    return a+b,a
result=addition(2,5)
print(result)


