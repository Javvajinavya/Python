#using normal for loop
print("")
list1=[]
for i in range(20):
    list1.append(i+1)
print(list1)
#using list comprehension
print("----------------------")
list2=[i+1 for i in range(20)]
print(list2)