#Positional
def pw(x,y):
    z=x**y
    print(z)
pw(2,4)
#Keyword
def Show(Name,age):
    print(Name,age)
Show(Name='Lowki',age=20)
#Default
def Show(Name='Ram',age=20):
    print(Name,age)
Show()
#Variable length 
def add (*num):
    z=num[0]+num[1]
    print(z)
add(1,2)
#keyword variable length
def add(**num):
    z=num['a']+num['b']
    print(z)
add(a=1,b=2)