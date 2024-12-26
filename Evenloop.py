Num=int(input("Enter the value"))
#Using if condition
print("Using for with if condition statements")
for i in range(1,Num+1):
    if (i%2==0):
        print(i)

# Using range operation
print("Using For with range step size")
for i in range(2,Num+1,2):
    print(i)