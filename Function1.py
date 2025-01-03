#local and global variables
Num=25
def Value():
    Num=35
    print(Num)
Value()

#return statements
def display():
    return "Happy Morning"
result=display()
print(result)
#examples for return statements
def add(y):
    x=10
    c=x+y
    return c
sum=add(20)
print(sum)

def Sub(x):
    y=10
    c=x-y
    return c
sub=Sub(20)
print(sub)

#nested functions
def Disp():
    def Show():
        print("Show function")
    print("Disp function")
    Show()
Disp()
#example for parameterized function
def Add(a,b):
    return a+b
def Sub(a,b):
    return a-b
def Mul(a,b):
    return a*b
def Div(a,b):
    return a/b
Sum=Add(24,56)
print(Sum)
Differ=Sub(56,23)
print(Differ)
Multipy=Mul(34,6)
print(Multipy)
Division=Div(46,5)
print(Division)