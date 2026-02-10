# Example:
#     Input: n = 4, m = 5
#     Output: ['*****', '*****', '*****', '*****']
     
#     Input: n = 3, m = 2
#     Output: ['**', '**', '**']

def generate_rectangle_pattern(m,n):
    rectangle_squares=[]
    for i in range(1,m+1):
        rectangle_squares.append("*"*n)
    return rectangle_squares

m=int(input("Enter the number"))
n=int(input("Enter the number"))
print(generate_rectangle_pattern(m,n))

#Through loops only
m=int(input("Enter the number"))
n=int(input("Enter the number"))
for i in range(0,m):
    print("*"*n)