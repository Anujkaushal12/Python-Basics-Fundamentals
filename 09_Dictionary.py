#Creating Dictionaries
empty_dict={}
my_dict=dict()
print(type(empty_dict))
print(type(my_dict))

student={"name":"Anuj","Age":19,"Coures":'Btech-CSE'}
print(student)

student['name']="Mayank"

#Last updated key is used
print(student)

#Accessing dictionary elements
print(student["name"])
print(student["Age"])

#Accessing dictionary using get() method
print(student.get("name"))
print(student.get("Age"))
print(student.get("Proffession","Not occupied yet")) #if key value pair is not in dictionary it added it
print(student)

#Modifying dictionary elements
#Dictionaries are mutable,so you can add,update or delete elements
print(student)

student["Age"]=20
print(student)

student["address"]="India" #Add the written key-value pair
print(student)

del student["Age"] #Delete key-value pair
print(student)

#Dictionary methods

Keys=student.keys() #Get all the values in the dictionary
print(Keys)

Values=student.values() #Get all the values in the dictionary
print(Values)

pairs=student.items() #Get all the key value pairs in dictionary
print(pairs)

#Deep copy
student_copy=student
print(student)
print(student_copy)

print(student)
print(student_copy)

student_copy=student.copy() #Shallow Copy
student["name"]="Krish3"
print(student)
print(student_copy)

#Iterating over Dictionaries
#You can use loops to iterate over dictionaries,key,value

print(student)

#Iterating over Keys
for key in student.keys():
    print(key)

#Iterating over values
for value in student.values():
    print(value)

#Iterating over key-value pairs
for key,value in student.items():
    print(f"{key}:{value}")

#nested Dictionaries
students={
    "student1":{"Name":"mayank","Age":19},
    "student2":{"Name":"Anshu","Age":19}
}
print(students)

#Acessing nested dictionary
print(students["student2"]["Name"])
print(students["student2"]["Age"])

print(student.items())

#Iterating over nested dictionaries
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")

#Dictionary Comphrehension
square={ x:x**2 for x in range(5)}
print(square)

#Condition dictionary comprhension
even={x:x**2 for x in range(10) if x%2==0}
print(even)

#Practical Examples
numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)

nums = [2, 7, 11, 15]
target = 9

seen = {}  # Dictionary to store numbers and their indices

for i, num in enumerate(nums):
    needed = target - num
    if needed in seen:
        print([seen[needed], i])  # Print the indices when found
        break
    seen[num] = i
