Str=input("Enter the String :")
Str=Str.replace(' ','')
Alpha_count=0
Digit_count=0
Special_count=0
for i in Str:
    if i.isalpha():
        Alpha_count+=1
    elif i.isdigit():
        Digit_count+=1
    else:
        Special_count+=1
print("Alphabet in String are",Alpha_count)
print("Digit count",Digit_count)
print("Special Count",Special_count)