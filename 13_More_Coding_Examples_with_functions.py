#Temprature Conversion
def temp_conv(temp,unit):
    if unit == "C" or unit == "c":
        return (temp *9/5) +32
    if unit == "F" or unit == "f":
        return (temp -32)*5/9
print(temp_conv(77,"f"))
print(temp_conv(25,"c"))

#Password Strength Checker

def Pass_strngth_checker(Password):
    if len(Password)<8:
        return "Password Weak"
    if not any(char.isdigit() for char in Password):
        return "Password Weak"
    if not any(char.isupper() for char in Password):
        return "Password Weak"
    if not any(char.islower() for char in Password):
        return "Password Weak"
    if not any(char in "!@#$%^&*+-~" for char in  Password):
        return "Password Weak"
    return "Password is Strong"
print(Pass_strngth_checker("Kaushal@2007#"))

#Calculate the total cost of items in a shopping cart

def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item["price"]* item["quantity"]
    return total_cost

#Example Cart Data
cart=[
    {"name":"Apple", "price":0.5,"quantity":4},
    {"name":"Banana", "price":1.0,"quantity":12},
    {"name":"Guava", "price":9.0,"quantity":5}
]

#Calling the function 
total_cost=calculate_total_cost(cart)
print(total_cost)

#Checking if a number is a palindrome or not
def check_palindrome_or_not(Number):
    print(Number)
    if Number[::-1]==Number:
        return "Number is a plaindrome "
    else:
        return "Number is not a plaindrome "
        
print(check_palindrome_or_not("madam"))

#Calcualte a factorial of a number using recursion
def function_no(Number):
    if Number ==0:
        return 1
    else:
        return Number*function_no(Number-1)
print(function_no(4))

