# Example:
#     Input: 5
#     Output: ['1', '22', '333', '4444', '55555']
     
#     Input: 3
#     Output: ['1', '22', '333']

#1
#22
#333

#through loops only
n=int(input("Enter your number:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()

#Trhoguh functions 
def generate_right_angled_triangle(n):
    right_angled_triangle=[]
    for i in range(1,n+1):
        row=str(i)*i
        right_angled_triangle.append(row)
    return right_angled_triangle

n=int(input("Enter your number"))
print(generate_right_angled_triangle(n))