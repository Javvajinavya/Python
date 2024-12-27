Name=input("Enter the Student Name :")
Sub1=int(input("Enter the Subjevt1 marks :"))
Sub2=int(input("Enter the Subject2 Marks :"))
Sub3=int(input("Enter the Subject3 Marks :"))
print("Student Report Card:")
print("-------------------------")
print("Student name :",Name)
print("Subject1 Score:", Sub1)
print("Subject2 Score:",Sub2)
print("Subejct3 Score:",Sub3)
if (Sub1>=35 and Sub2>=35 and Sub3>=35):
    Total=Sub1+Sub2+Sub3
    print("Total :",Total)
    Average=(Total)//3
    print("Average:", Average)
    if (Average>=90):
        print("Congratulations You Have Qualified With 1st Class")
    elif (Average>=75):
        print("Congratulations You Have Qualified With 2nd Class")
    else :
        print("Congratulations You Have Qualified With 3rd Class")
else:
    print("Failed")
