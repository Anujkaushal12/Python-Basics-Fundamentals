# Problem Description:
# You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The triangle has '*' characters, starting with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.

# Input Parameters:
#                  n (int): The height and base of the right-angled triangle.


# Output:
#        A list of strings where each string is a row of '*' characters that increases in length from 1 to n.

# Example:
#     Input: 3
#     Output: ['*', '**', '***']
     
#     Input: 5
#     Output: ['*', '**', '***', '****', '*****']

#By loop only
n=int(input("Enter your number"))
for i in range(1,n+1):
    print("*"*i)

#through functions
def generate_right_angled_triangle(n):
    right_angled_triangle_squares=[]
    for i in range(1,n+1):
        right_angled_triangle_squares.append("*"*i)
    return right_angled_triangle_squares

n=int(input("Enter your number"))
print(generate_right_angled_triangle(n))