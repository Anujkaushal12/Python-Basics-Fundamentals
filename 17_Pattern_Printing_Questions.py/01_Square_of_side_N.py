# Example:
#     Input: 3
#     Output: ['***', '***', '***']
     
#     Input: 5
#     Output: ['*****', '*****', '*****', '*****', '*****']

#Through loops only
n=int(input("Enter your number:"))
for i in range(1,n+1):
    print("*"*n)


#Thrpough functions
def generate_square(n):
    squares=[]
    for i in range(1,n+1):
        squares.append("*"*i)
    return squares
n=int(input("Enter your number"))
print(generate_square(n))

