n=5
spaces=8
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    for k in range(spaces):
        print(" ",end="")
    for l in range(0,i+1):
        print("*",end="")
    print("")
    spaces-=2

spaces1=2
for a in range(0,n-1):
    for b in range(n-a-1):
        print("*",end="")
    for c in range(spaces1):
        print(" ",end="")
    for d in range(0,n-a-1):
        print("*",end="")
    print("")
    spaces1+=2