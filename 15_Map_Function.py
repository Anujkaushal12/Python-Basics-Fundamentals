# The map() function applies a given function to all items in an input list (or any other iterable) and returns a map object (an iterator). This is particularly useful for transforming data in a list comprehensively.


def square(x):
    return x**2
print(square(10))

#Squaring of number thorugh map function
numbers=[10,20,30,40,50]
squared_nos=list(map(square,numbers))
print(squared_nos)

#Map() function with lambda function
nos=(5,10,15,20,25,30)
cube_no=list(map(lambda x:x**3,nos))
print(cube_no)

#MAp multiple iterables
numbers1=[1,2,3]
numbers2=[4,5,6]

added_numbers=list(map(lambda x,y:x+y,numbers1,numbers2))
print(added_numbers)

## map() to convert a list of strings to integers
# Use map to convert strings to integers
str_numbers = ['1', '2', '3', '4', '5']
int_numbers = list(map(int, str_numbers))

print(int_numbers)

#Converting the list iterables into upper character
words=['apple','banana','cherry']
upper_word=list(map(str.upper,words))
print(upper_word)

dict=[
    {"name":"anuj","age":19},
    {"name":"anshu","age":18}
]
add_lastname=list(map(lambda adds:adds["name"],dict))
print(add_lastname)
