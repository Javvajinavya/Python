for i in range(101,1000):
    hundreds=i//100
    tens=(i//10)%10
    ones=i%10
    if(hundreds==ones):
        print(i)

#Using double for 
for i in range(1,10):
    for j in range(0,10):
        print(i,j,i)