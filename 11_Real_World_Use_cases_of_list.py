#Example1
#Creating a to do
to_do_list=["Buy groceries","Clean the house","Pay bills","Finish project","Call mom"]
print("To-Do List:")
for index,task in enumerate(to_do_list, start=1):
    print(f"{index}.{task}")

#Example2
#organizing student grades
student_grades={
    "Alice":85,
    "Bob":92,
    "Charlie":78,
    "Diana":90,
    "Ethan":88
}
print("\nStudent Grades:")
for student,grade in student_grades.items():
    print(f"{student}: {grade}")   

#Example3
#Inventory management

Inventory=["Apples","Bananas","Oranges","Grapes","Mangoes"]

#Adding new item in an inventory list
Inventory.append("Watermelon")

#Required item from an inventory
required_item=input("Enter your item")

if required_item in Inventory:
    print(f"Yes, Required items is in stock which is {required_item}")
else:
    print(f"No, Required item is not in stock which is {required_item}")

print("Items that are in inventory:")
for item in Inventory:
    print(f"->{item}")

#Example4
#Collecting user feedback

All_feedback=["Great Experience","Not Satisfied","Could be better","Excellent service"]

positive_feedback_count=sum(1 for comment in All_feedback if "great" in comment.lower() or "excellent" in comment.lower())
print(f"{positive_feedback_count}")

#Printing all feedback
print("User Feedback")
for comment in All_feedback:
    print(f"-{comment}")