# Example:
#     Input: 3
#     Output: ['***', '**', '*']
     
#     Input: 5
#     Output: ['*****', '****', '***', '**', '*']

#Through loops only
n=int(input("enter your number"))
for i  in range(n,0,-1):
    print("*"*i)

#through fucntions
def generate_inverted_right_angled_triangle(n):
    inverted_right_angled_triangle=[]
    for i in range(n,0,-1):
        inverted_right_angled_triangle.append("*"*i)
    return inverted_right_angled_triangle

n=int(input("Enter your number"))
print(generate_inverted_right_angled_triangle(n))



