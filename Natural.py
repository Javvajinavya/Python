Num=int(input("Enter the Integer value"))
if Num<0:
    print("Enter the positive number")
else:
    sum=0
    while(Num>0):
        sum=sum+Num
        Num=Num-1
    print("The Sum of N natural Numbers are", sum)


#for loop
N=int(input("Enter the number"))
sum=0
for i in range(1,N+1):
    sum=sum+i
print(sum)