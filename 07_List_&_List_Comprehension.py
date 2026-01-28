lst=[]
print(type(lst))

names=["Anuj","Shaurya",98,True,45.3]
print(names)

#Accessing List Elements

fruits=["Apple","Banana","Grapes","Cranberry"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

#Slicing list elements
print(fruits[0:2])
print(fruits[2:0])
print(fruits[-1:-3])
print(fruits[::-1])

#Modifying the list elements

fruits[0]="Watermelon"
print(fruits)

fruits[:]="Tomato"
print(fruits)

#Functions of list elements
Car=["Defender","Porsche","Rolls-Royce","Lamborghini-urus","Range-Rover"]

print(len(Car))

Car.append("Altroz") #Add one element at the end of the list
print(Car)

Car.extend(["Alto","Swift-Dzire"]) #Add 2 or more elements at the end of the list
print(Car)

Car.insert(2,"Fortuner") #Insert the element at the mentioned index
print(Car)

Car.remove("Alto")
print(Car)

Car.pop() #Removes and returns the last element in the list
Car.pop(2) #Removes and returns the element at mentioned index
print(Car)

Index_of_specific_element=Car.index("Rolls-Royce")
print(Index_of_specific_element)

list20=[3,2,5,2,3,2,5,1,4]
print(list20.index(3,3))

No_of_times_element_occurs=Car.count("Defender") #How many times element occur in the list
print(No_of_times_element_occurs)

Car.sort()#Arrange the element in ascending order on the basis of 
print(Car)

Car.sort(reverse=True)#Arrange the element in descending order on the basis of 
print(Car)

Car.reverse()##Arrange the element in desending order on the basis o
print(Car)

print(min(Car))

print(max(Car))

Copy_of_original=Car.copy()#Swallow copy
Copy_of_original.append("G-Wagon")
print(Car)#Not appended the element appended in copy_of_original
print(Copy_of_original)#"G-Wagon appended in this list"

Copy_of_original=Car#deep copy
Copy_of_original.append("maclren")
print(Car)#Both of the list had appended the maclren
print(Copy_of_original)#Both of the list had appended the maclren


Car.clear()#clear the list
print(Car)


#Iterating over list
names=["Anuj","Dhananjay","Dhoni","Aditya"]
for name in names:
    print(name)

#Iteration over list with index
for index,name in enumerate(names,start=0):  #A Python tool that allows you to loop through an iterable like a (list, tuple, or string) and have access to both the index and the element itself
    print(f"At index {index} name is {name}")

#List comphrehension
numbers=[10,20,30,40,50]
even_numbers=[number for number in numbers if number%2==0]
print(even_numbers)


#Nested list comphrehension
lst1=[1,2,3,4]
lst2=["a","b","c","d"]
pair=[[i,j] for i in lst1 for j in lst2]
print(pair)

#List comphrehension with function call
words=["hello","anuj","how","are","you"]
lengths=[len(word) for word in words]
print(lengths)

