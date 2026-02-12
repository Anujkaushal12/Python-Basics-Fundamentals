# Example:
#     Input: 5
#     Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']
     
#     Input: 3
#     Output: ['1', '2 3', '4 5 6']

#through loops
n=int(input("Enter your number"))
val=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(val,end=" ")
        val+=1
    print()



