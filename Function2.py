def Multiplication_table(n):
    for i in range(1,11):
        print(n,"X",i,"=",(n*i))
    print("------------------------")
Multiplication_table(2)
Multiplication_table(3)


#to print  1 to n tables
def Multiply(n):
    for i in range(1,n+1):
        for j in range(1,11):
            print(i,"X",j,"=",(j*i))
    print("------------------------")
Multiply(3)

#
def Display(n):
    print("I am the first function")
    n()
def One():
    print("I am the frist nested function")
def Two():
    print("Im the second nested function")
Display(One)
Display(Two)

#Aruguments
