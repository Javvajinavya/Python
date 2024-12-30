Prog=('Python','C','C++','Java','Angular','React','Javacript','Dark','Html','Css')
print("The original tuple is---------------")
print(Prog)
print("Accessing elements using positive--------")
print(Prog[0])
print(Prog[1])
print(Prog[2])
print(Prog[3])
print(Prog[4])
print(Prog[5])
print("Accessing the elements using negative indexing-------")
print(Prog[-1])
print(Prog[-1])
print(Prog[-3])
print(Prog[-4])
print("Accessing lements through the loops-------------")
print("Acessing using for loops------------------------")
for i in Prog:
    print(i)
print("Accessing tuple using while loop-----------------")
i=0
while (i<len(Prog)):
    print(Prog[i])
    i+=1

