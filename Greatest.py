Num1=int(input("Enter the first Number"))
Num2=int(input("Enter the second number"))
if Num1>Num2:
    print(Num1," is greatest number")
else:
    print(Num2,"is greatest number")

#terninary
Result= "Num1 is greatest number" if (Num1>Num2) else "Num2 is greatest"
print(Result)