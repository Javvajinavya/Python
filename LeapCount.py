Year=int(input("Enter the Year"))
LeapCount=0
Count=20
print("Leap Years Are: ")
while(LeapCount!=Count):
    if (Year%4==0 and Year%100!=0) or ((Year%400==0)):
        LeapCount+=1
        print(Year)
    Year+=1