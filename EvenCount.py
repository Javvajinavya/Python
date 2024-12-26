N=int(input("Enter the Number"))
EvenCount=0
for i in range(1,N+1):
    if (i%2==0):
        EvenCount=EvenCount+1
print("Even Number",EvenCount)