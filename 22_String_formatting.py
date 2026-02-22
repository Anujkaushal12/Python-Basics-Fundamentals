person={"name":"Anuj","age":18}

sentence="My name is " + person["name"] + " and I am " + str(person["age"]) + " years old"
print(sentence)

sentence1="My name is {0} and I am {1} years old".format(person['name'],person['age'])
print(sentence1)

sentence2="My name is {0[name]} and I am {1[age]} years old".format(person,person)
print(sentence2)

sentence3="My name is {0[name]} and I am {0[age]} years old".format(person)
print(sentence3)

sentence4="My name is {0[name]} and I am {0[age]} years old".format(person)
print(sentence4)

l=["Mayank","20"]
meaning="My name is {0[0]} and I am {0[1]} years old".format(l)
print(meaning)

class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person("Divyansh",19)

sentence6="My name is {0.name} and I am {0.age} years old".format(p1)
print(sentence6)

sentence="My name is {name} and I am {age} years old".format(name="anuj",age=18)
print(sentence)

person={"name":"Anuj","age":18}
sentence="My name is {name} and I am {age} years old".format(**person)
print(sentence)

pi=3.14159265
sentence="Pi value is equal to {:.2f}".format(pi)
print(sentence)

sentence="1 Mb is equal to {:,.2f} bytes".format(1000**2)
print(sentence)

import datetime
my_date=datetime.datetime(2026,2,22, 21,55,00)
print(my_date)

sentence="{0:%B %d, %Y} fell on {0:%A} day of the year is {0:%j}".format(my_date)
print(sentence)