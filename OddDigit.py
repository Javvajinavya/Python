Num=int(input("Enter the Integer value: "))
OddDigitCount=0
Rem=0
while(Num!=0):
    Rem=Num%10
    if(Rem%2!=0):
        OddDigitCount+=1
    Num=Num//10
print("Number of Odd Digits",OddDigitCount)