Dict={101:'Python',102:'Sql',103:'C',104:'Html'}
print("The original dictionary is:-------")
print(Dict)
print(type(Dict))
print("-----------------")
print(Dict[101])
print(Dict[102])
print(Dict[103])
print(Dict[104])
Dict[105]='Java'
print(Dict)
print("-----------------")
Dict[101]='Flutter'
print(Dict)
del Dict[102]
print(Dict)
del Dict
