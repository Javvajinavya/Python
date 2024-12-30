Str=input("enter the string :")
Vowel_Count=0
Consonent_Count=0
Str=Str.lower()
Str=Str.replace(' ','')
for i in Str:
    if (i in ('a','e','i','o','u')):
        Vowel_Count+=1
    elif i.isalpha():
        Consonent_Count+=1
print("Number of Vowels in given String are:",Vowel_Count)
print("Number of Consonents in given String are:",Consonent_Count)