Num=int(input("Enter the Integer Value"))
Sum_Digits=0
Remainder=0
while(Num!=0):
    Remainder=Num%10
    Sum_Digits=Sum_Digits+Remainder
    Num=Num//10
print("The Summation of Digits in given Integer Value is ",Sum_Digits)