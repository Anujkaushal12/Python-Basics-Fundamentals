# Example:

#     Input: 3
#     Output: ['*****', ' *** ', '  *  ']
     
#     Input: 5
#     Output: ['*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']


#*****  n=3
# ***
#  *

#loops only
n=int(input("Enter your number"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")

    for k in range(2*i-1):
        print("*",end="")
    print()
 
#Functions only
def generate_inverted_pyramid_pattern(n):  #n=3
    inverted_pyramid_pattern=[]
    for i in range(0,n): #n=3
        star="*"*(n*2-1)
        spaces=" "*i
        inverted_pyramid_pattern.append(spaces+star+spaces)
    return inverted_pyramid_pattern

n=int(input("Enter your number"))
print(generate_inverted_pyramid_pattern(n))