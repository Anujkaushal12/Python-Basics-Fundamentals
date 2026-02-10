def generate_hollow_square(n):
    hollow_squares=[]
    for i in range(0,n):
        if i==0 or i==n-1:
            hollow_squares.append("*"*n)
        else:
            hollow_squares.append("*"+" "*(n-2) +"*")
    return hollow_squares

n=int(input("Enter your number"))
print(generate_hollow_square(n))

#Through loops only
n=int(input("Enter your number"))
for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")