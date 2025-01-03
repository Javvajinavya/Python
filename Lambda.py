#lambda function for single arguments
Result=lambda Num:print(Num)
Result(100)

#lambda Function of more than one arguments
Result=lambda a,b:print(a*b)
Result(10,5)

#two varibale
add_sub=lambda x,y:(x+y , x-y)
a,s=add_sub(7,5)
print(a)
print(s)