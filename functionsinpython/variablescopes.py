# there are 4 variable scopes in python 1. local variable 2. global variable 3.enclosed variable 4. built in variable

a=1
b=2
def func():
    print(a)
    b=1
    print(b)
func()
# in the above function a is a glabal variable and b is local variable

def func_1():
    global b
    print(b)
func_1()
# in the above function func_1 is a global b variable

def red():
    a=1
    def blue():
        b=1
        print(a)
        print(b)
    blue()
    print(a)
red()
# in the above function red and blue is enclosing function
