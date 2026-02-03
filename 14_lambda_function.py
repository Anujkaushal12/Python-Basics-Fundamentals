# Lambda functions are small anonymous functions defined using the **lambda** keyword. They can have any number of arguments but only one expression. They are commonly used for short operations or as arguments to higher-order functions.

#Syntax
lambda argument: expression

#Function
def mul(a,b):
    return a*b
print(mul(3,4))

#Multiplication of 2 arguments Through lambda function
mul=lambda a,b: a*b
print(mul(3,4))

#Printing even no through lambda function
even_no=lambda x: x%2==0
print(even_no(10))

#Addition of 3 arguments through normal function
def add(x,y,z):
    return x+y+z
print(add(3,4,5))

#Addition of 3 arguments through lambda function
add=lambda x,y,z: x+y+z
print(add(8,5,4))