Num=int(input("Enter the Number"))
EvenSum=0
OddSum=0
for i in range(1,Num+1):
    if (i%2==0):
        EvenSum=EvenSum+i
    else:
        OddSum=OddSum+i
print("Sum of even number",EvenSum)
print("Sum of Odd Numbers", OddSum)