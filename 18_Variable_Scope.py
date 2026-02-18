'''
LEGB
LOCAL,ENCLOSING,GLOBAL,BUILT-IN
'''

#Global and local Scope
x="Global variable"
def test(z):
    # global x
    x="local variable"
    print(x)
    print(id(x))
    # global y
    y="local variable"
    print(y)
test("local var")
# print(x)
print(x)
print(id(x))

#Built-in scope
import builtins
print(dir(builtins))

#Enclosign scope

x="Global Scope"

def func():
    y="outer scope"
    def func1():
        # z="inner scope"
        # print(z)
        print(y)
    func1()
    # print(y)
    print(x)
func()
print(x)