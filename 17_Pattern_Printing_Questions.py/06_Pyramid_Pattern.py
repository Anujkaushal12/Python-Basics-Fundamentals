# Example:

#     Input: 3
#     Output: ['  *  ', ' *** ', '*****']
     
#     Input: 5
#     Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']

#Through loops
n=int(input("Enter your number"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")

    for k in range(1,2*i):
        print("*",end="")
    print()

#Through function
def generate_pyramid_pattern(n):
    pyramid_pattern=[]
    for i in range(0,n):
        star="*"*(2*i+1)
        spaces=" "*(n-i-1)
        pyramid_pattern.append(spaces+star+spaces)
    return pyramid_pattern

n=int(input("Enter your number"))
print(generate_pyramid_pattern(n))