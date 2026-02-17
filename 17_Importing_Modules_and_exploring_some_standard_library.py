# import my_module as mm,test
#OR
from my_module import find_index as fi,test

courses=["Btech","Bca","Bsc"]
index=fi(courses,"Btech")
print(index)
print(test)

import random
print(random.choice(courses))

import math
pie=math.radians(22/7)
print(pie)

import datetime
import calendar

curr_time=datetime.date.today()
print(curr_time)

years=calendar.isleap(2000)
print(years)

import os
print(os.getcwd()) #current working directory path
print(os.__file__) #current working file path