#Create a set
my_set={1,2,3,4,5}
print(my_set)
print(type(my_set))

my_empty_set=set()
print(type(my_empty_set))

my_set=([1,2,3,4,5,6])
print(my_set)

#Repeatex Elements
my_empty_set=set([1,2,3,4,5,6])
print(my_empty_set)

#Basic sets operation 

#Adding the elements
my_empty_set.add(7)
print(my_empty_set)

#Removing the element from the set
my_empty_set.remove(7)
print(my_empty_set)

#my_empty_set.remove(10)#This gives an error because its already removed
#print(my_empty_set)

#So For getting this executed we use discard method it run the program without getting error when that element is not in a set.
my_empty_set.discard(10)
print(my_empty_set)

#Pop() method
my_empty_set.clear()
print(my_empty_set)

#Set Membership Test
a={1,2,3,4,5,6}
if 3 in a:
    print("3 is in the above set")

#Sets Mathematical Operations
set1={1,2,3,4,5,6,7}
set2={4,5,6,7,8}
set3={7,8,9,10}

#Union() Method
union_set=set1.union(set2)
print(union_set)

#Intersection() method
intersection_set=set1.intersection(set2)
print(intersection_set)

set1.intersection_update(set2,set3)
print(set1)

set4={1,2,3,4,5,6}
set5={5,6,7,8,9}

#Difference
print(set4.difference(set5)) #It given the only that element of set1 that are not in set2.

#Sets Methods

set7={1,2,3,4,5}
set8={3,4,5}

#issubset method
print(set7.issubset(set8))

#issuperset method
print(set7.issuperset(set8))