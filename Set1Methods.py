a={'Rahul','Raj','Sonam','Rani'}
b={'Sunil','Rahul','Rani','Python','Java'}
print("The original sets are:-----------")
print("A",a)
print("B",b)
print("The intersection of the set-----")
ism=a.intersection(b)
print("Intersection:",ism)
print("The union os the set -----------")
um=a.union(b)
print("Union:",um)
print("The differebnce of set :-----------")
dm=a.difference(b)
print("Difference:",dm)
print("the subset of the set-----------")
isub=a.issubset(b)
print(" subset:",isub)
print("The superset of the set-------------")
isup=b.issuperset(a)
print("Is superset:",isup)