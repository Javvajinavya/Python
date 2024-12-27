Num=int(input("Enter the Integer Value"))
Num1=Num
Rem=0
Reversed=0
for i in range(2,Num1):
        if(Num1%i==0):
            print("its not a prime plaindrome")
            break
else:
    while(Num!=0):
        Rem=Num%10
        Reversed=Reversed*10+Rem
        Num=Num//10
    if(Num1==Reversed):
        print("Its a prime palindrome")
    else:
         print("Its not a prime palindrome")
   
