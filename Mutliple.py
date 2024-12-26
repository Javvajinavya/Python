Num=int(input("Enter the integer value"))
if (Num%3==0 and Num%5==0):
    print("multiple of 3&5 ")
else:
    print("not a multiple of 3&5")

#terninary
Result= "Multiple of 3&5" if (Num%3==0 and Num%5==0) else "Not a multiple of 3&5"
print(Result)