#input() function is a built-in method used to get data from a user during the execution of a program. 
first_name=input("Enter your first name")
last_name=input("Enter your last name")
print(first_name,last_name)

#int(input()) is a common way to take user input from the console and convert it immediately into an 
#integer data type.
school_roll_no=int(input("Enter your School name"))
print(school_roll_no)

#float(input()) is a common way to take user input from the console and convert it immediately into 
#an integer data type.
Marks=float(input("Enter your marks:"))
print(Marks)

# The sep argument defines the string that is inserted between the items passed to the
#print() function. It allows for customized output formatting beyond the default spacing.
print(first_name,last_name,school_roll_no,Marks,sep=",")