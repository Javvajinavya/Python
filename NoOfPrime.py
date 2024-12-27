num=int(input("Enter the integer value:"))
Count=0
for i in range(2,num+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)