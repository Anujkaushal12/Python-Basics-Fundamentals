#*******
# *****
#  ***
#   *     n=5
#  ***
# *****
#*******

#through while loop
n = int(input("Enter your number: "))

i = n
while i > 0:
    j = 0
    while j < (n - i):
        print(" ", end="")
        j += 1
    k = 0
    while k < (2 * i - 1):
        print("*", end="")
        k += 1
    print()
    i -= 1

p = 2
while p <= n:
    q = 0
    while q < (n - p):
        print(" ", end="")
        q += 1
    r = 0
    while r < (2 * p - 1):
        print("*", end="")
        r += 1
    print()
    p += 1


