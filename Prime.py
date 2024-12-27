Num=int(input("Enter the integer value:"))
Count=0
for i in range(1,Num+1):
    if(Num%i==0):
        Count+=1
if(Count==2):
    print("Prime Number")
else:
    print("Not a Prime Number")

#---------------
for i in range(2,Num):
    if(Num%i==0):
        break
else:
    print("Prime Number")


#