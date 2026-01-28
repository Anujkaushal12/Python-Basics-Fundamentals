#Creating a tuple
empty_tuple=()
print(empty_tuple)
print(type(tuple))

numbers=tuple([1,2,3,4,5,6])
print(numbers)

list((1,2,3,4,5,6))

mixed_tuple=(1,"Hello World",3.14,True)
print(mixed_tuple)

#Accesing Tuple Elements
print(numbers)

print(numbers[2])
print(numbers[-1])

print(numbers[0:4])

print(numbers[::-1])

#Tuple Operations

concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple)

print(mixed_tuple * 3)

print(numbers * 3)

#Immutable Nature of Tuples
#Tuples are immutable, meaning their elements cannot be changed once assigned.

lst=[1,2,3,4,5,6]
print(lst)

lst[1]="Anuj Kaushal"
print(lst)

print(numbers)

#Tuple Methods
print(numbers.count(1))
print(numbers.index(3))

#Packing and Unpacking tuple

#packing
packed_tuple=1,"Hello",3.14
print(packed_tuple)

#Unpacking
a,b,c=packed_tuple
print(a)
print(b)
print(c)

#Unpacking with *
numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(first)
print(middle)
print(last)

#Nested Tuple
#Nested List
lst=[[1,2,3,4],[6,7,8,9],[1,"Hello",3.14,"c"]]
print(lst[0][0:3])

lst=[[1,2,3,4],[6,7,8,9],(1,"Hello",3.14,"c")]
lst[2][0:3]

nested_tuple=((1,2,3),("a","b","c",(True,False)))

#Access the elements inside a tuple
print(nested_tuple[0])
print(nested_tuple[1],[2])


nested_tuple=((1,2,3),("a","b","c"),(True,False))

#Iterating over nested tuples
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item,end=" ")
    print()

