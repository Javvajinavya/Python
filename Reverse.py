Num=int(input("Enter the Number"))
Reaminer=0
Reversed_number=0
while(Num!=0):
    Remainder=Num%10
    Reversed_number=Reversed_number*10+Remainder
    Num//=10
print("Reversed number:", Reversed_number)