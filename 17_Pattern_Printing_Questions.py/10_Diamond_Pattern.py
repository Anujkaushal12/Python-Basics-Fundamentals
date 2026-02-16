# Example:
#     Input: 3
#     Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
     
#     Input: 5
#     Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']

#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *

n=int(input("Enter your number:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()

for p in range(1,n):
    for q in range(1,p+1):
        print(" ",end="")
    for r in range(1,2*(n-p)):
        print("*",end="")
    print()
    