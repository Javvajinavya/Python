#using length funtion
List=['Navya','Lowkika','Meghana','Akshay']
for i in List:
    if (len(i)==5):
        print(i)
A=min(List)
print("Minimum element:",A)
print(max(List))
List.sort()
print("Sorted list:",List)
List.reverse()
print("Reversed list:",List)
