Str=input("Enter the string")
print("The user entered String is",Str)
if Str.isalpha():
    print("The entered String is Alphabet")
elif Str.isdigit():
    print("The user enetered String is Digit")
elif Str.isdecimal():
    print("The user enetered String is Decimal")
else:
    print("The user enetered String is rather than these three")
