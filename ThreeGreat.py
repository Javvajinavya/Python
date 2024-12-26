Num1=int(input("Enter the first Number"))
Num2=int(input("Enter the second number"))
Num3=int(input("Enter the third number"))
if (Num1>Num2 and Num1>Num3):
    print("Num1 is greatest number")
elif (Num2>Num1 and Num2>Num3):
    print("Num2 is greatest number")
else:
    print("Num3 is greatest number")

Result= "Num1 is Smallest number" if (Num1>Num2 and Num1>Num3) else "Num2 is Smallest number " if (Num2>Num1 and Num2>Num3) else "Num3 is smallest number"
print(Result)
