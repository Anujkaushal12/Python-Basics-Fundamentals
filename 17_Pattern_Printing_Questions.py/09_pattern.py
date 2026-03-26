# n=5
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

n=int(input("Enter your number"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,(2*i)):
        print("*",end="")
    print()

for p in range(1,n+1):
    for m in range(1,p):
        print(" ",end="")
    for l in range(0,(2*n)-((2*p)-1)):
        print("*",end="")
    print()
