# n=5
#    *
#   ***
#  *****
# *******

n=int(input("enter your number"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range((2*i)-1):
        print("*",end="")
    print()