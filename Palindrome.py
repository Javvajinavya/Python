Num=int(input("Enter the Number"))
Num1=Num
Rem=0
Reversed=0
while(Num!=0):
    Rem=Num%10
    Reversed=Reversed*10+Rem
    Num//=10
if (Num1==Reversed):
    print(Num1,"is a plaindrome Number")
else:
    print(Num1,"is not a palindrome")