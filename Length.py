Num=int(input("enter the value"))
DigitCount=0
while(Num!=0):
    Num=Num//10
    DigitCount+=1
print(DigitCount,"Digits")