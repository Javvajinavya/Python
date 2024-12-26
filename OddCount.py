N=int(input("Enter the Number"))
OddCount=0
for i in range(1,N+1):
    if (i%2!=0):
        OddCount=OddCount+1
print("Odd Number",OddCount)