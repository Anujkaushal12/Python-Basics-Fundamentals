n=5
for i in range(0,n):
    for j in range(n-i):  #stars
        print("*",end="")
    for k in range(2*i): #spaces
        print(" ",end="")
    for j in range(n-i):  #stars
        print("*",end="")
    print("")

spaces=8
for a in range(0,n):
    for b in range(a+1):
        print("*",end="")
    for c in range(spaces):
        print(" ",end="")
    for d in range(a+1):
        print("*",end="")
    print("")
    spaces=spaces-2