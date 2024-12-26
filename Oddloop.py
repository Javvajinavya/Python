Num=int(input("Enter the value"))
#using for with if
print("Using for with if condition")
for i in range(1,Num+1):
    if (i%2!=0):
        print(i)


#using for with step size
print("Using for with rangee step size")
for i in range(1,Num+1,2):
    print(i)