nums=[1,2,3,4,5,6,7,8,9]

#I want 'n*n' for each n' in nums
my_list=[]
for n in nums:
    my_list.append(n)
print(my_list)

my_list=[n for n in nums]
print(my_list)

my_list=list(map(lambda x:x*x,nums))
print(my_list)

#we want number who are even
my_list=list(filter(lambda x:x%2==0,nums))
print(my_list)


#Dictionary Comprehension
names=["anuj","mayank","prashant","divyansh"]
heroes=["Spider-man","batman","superman","ronaldo"]
print(list(zip(names,heroes)))

my_dict={}
for names,heroes in zip(names,heroes):
    my_dict[names]=heroes
print (my_dict)

my_dict={names:heroes for names,heroes in zip(names,heroes)}
print (my_dict)


#Set Comprehension
# nums=[1,2,3,4,5,6,7,8,9]

nums=[1,1,2,1,5,3,5,2,7,9,7,6,4]
my_set=set()
for num in nums:
    my_set.add(num)
print(my_set)

my_set={n for n in nums}
print (my_set)