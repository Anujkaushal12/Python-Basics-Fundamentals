#Sorted list

lst=[9,1,8,2,3,5,6,3,6]

s_lst=sorted(lst)

print("Original list",lst)
print("Sorted list",s_lst)

lst.sort()
print(lst) 

#Sorted Tuple
tup=(9,3,5,7,2,1,8,6)

s_tup=sorted(tup)
print("Sorted Tuple",s_tup)

s_tup1=sorted(tup,reverse=True)
print("Descending sorting",s_tup1)

#Dictionary Sorting
dict={"name":"anuj","course":"BTECH","age":19}

dict1=sorted(dict)
print(dict1)

dict2=sorted(dict,reverse=True)
print(dict2)

#
class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def __repr__(self):
        return "{},{},{}".format(self.name,self.age,self.salary)

from operator import attrgetter

e1=Employee("Carl",35,53000)
e2=Employee("Sarah",19,80000)
e3=Employee("Anuj",20,95000)

employees=[e1,e2,e3]

# def e_sort(emp):
#     return emp.salary

s_employees=sorted(employees, key=attrgetter("age"))

print(s_employees)