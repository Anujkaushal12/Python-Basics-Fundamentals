n=int(input("Enter no:"))
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    ch="A"
    brkpnt=(2*i+1)/2
    for k in range(0,2*i+1):
        print(ch,end="")
        if (k <=brkpnt):
            ch=chr(ch+1)
        else:
            ch=chr
    for l in range(0,n-i):
        print(" ",end="")
    print("")