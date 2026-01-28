## Declaring And Assigning Variables

age=32
height=6.1
name="Krish"
is_student=True

## printing the variables

print("age :",age)
print("Height:",height)
print("Name:",name)

## Naming Conventions
## Variable names should be descriptive
## They must start with a letter or an '_' and contains letter,numbers and underscores
## variables names case sensitive

#valid variable names

first_name="KRish"
last_name="Naik"

# Invalid variable names
#2age=30
#first-name="Krish"
##@name="Krish"

## case sensitivity
name="Krish"
Name="Naik"

## Understnading Variable types
## Python is dynamically typed,type of a variable is determined at runtime
age=25 #int
height=6.1 #float
name="KRish" #str
is_student=True #bool

print(type(name))

## Type Checking and Conversion

type(height)

age=25
print(type(age))

# Type conversion
age_str=str(age)
print(age_str)
print(type(age_str))

age='25'
print(type(int(age)))

name="Krish"
type(name)

height=5.11
type(height)

float(int(height))

## Dynamic Typing
## Python allows the type of a vraible to change as the program executes
var=10 #int
print(var,type(var))

var="Hello"
print(var,type(var))

var=3.14
print(var,type(var))


age=int(input("What is the age"))
print(age,type(age))

### Simple calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)


##DATA TYPES

## Integer Example
age=35
type(age)

##floating point datatype
height=5.11
print(height)
print(type(height))

## string datatype example
name="Krish"
print(name)
print(type(name))

## boolean datatype
is_true=True
type(is_true)

a=10
b=10

type(a==b)

## common errors

#result="Hello" + 5 #error bcz string and int does not concatenate
result="Hello" + str(5)
print(result)


##Swap Variables
a=10
b=20
print(a,b)
a,b=b,a
print(a,b)

#Memory behaviour of string and integer