# n=5
# *********
#  *******
#   *****
#    ***
#     *

n=int(input("Enter your number"))
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(1,(2*n)-(2*i+1)+3):
        print("*",end="")
    print()