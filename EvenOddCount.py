Num=int(input("Enter the Integer value"))
EvenCount=0
OddCount=0
for i in range(1,Num+1):
    if (i%2==0):
        EvenCount=EvenCount+1
    else:
        OddCount=OddCount+1
print("Even Numbers From 1 to N are ", EvenCount)
print("Odd Numbers From 1 to N are", OddCount)