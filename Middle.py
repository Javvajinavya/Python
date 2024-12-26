Num1=int(input("enter the first number"))
Num2=int(input("Enter the seond number"))
Num3=int(input("Enter the third number"))
if (Num1>Num2 and Num1<Num3) or (Num1>Num3 and Num1<Num2):
    print("Num1 is middle")
elif (Num2>Num1 and Num2<Num3) or (Num2>Num3 and Num2<Num1):
    print("Num2 is middle")
else:
    print("Num3 is middle")

    #ternary
Result="Num1 i middle" if ((Num1>Num2 and Num1<Num3) or (Num1>Num3 and Num1<Num2)) else "Num2 is middle " if ((Num2>Num1 and Num2<Num3) or (Num2>Num3 and Num2<Num1)) else "Num3 is middle"
print(Result)