Name=input("Enter The Employee Name :")
Designation=input("Enter the Employee Designation :")
Salary=int(input("Enter the Salary :"))
Special_Allowances=int(input("Enter the Specail Aloowances :"))
Bonus=int(input("Enter the Bonus for Employee :"))
Taxable_Income=0
Annual_Income=0
print("Employee Details")
print("----------------------------------")
print("Employee Name :",Name)
print("Designation of Employee :", Designation)
print("Salary :",Salary)
print("Special Allowances :",Special_Allowances)
print("Bonus for Employee :", Bonus)
#Calculating Gross Monthly Salary
Gross_Monthly_Salary=(Salary+Special_Allowances)
print("Gross Monthly Salary:",Gross_Monthly_Salary)
#calculating Gross Annual Salary
Gross_Annual_Salary=(Gross_Monthly_Salary+Bonus)
print("Gross Annual Salary", Gross_Annual_Salary)
if (Gross_Annual_Salary>=500000):
    Taxable_Income=(Gross_Annual_Salary*15)//100
    print("Taxable Income",Taxable_Income)
    Annual_Income=(Gross_Annual_Salary-Taxable_Income)
    print("Annual Income of Employee",Annual_Income)
elif (Gross_Annual_Salary>=500000):
    Taxable=(Gross_Annual_Salary*10)//100
    print("Taxable Income",Taxable_Income)
    Annual_Income=(Gross_Annual_Salary-Taxable_Income)
    print("Annual Income of Employee",Annual_Income)
else:
    Taxable_Inc=(Gross_Annual_Salary*2)//100
    print("Taxable Income",Taxable_Income)
    Annual_Income=(Gross_Annual_Salary-Taxable_Income)
    print("Annual Income of Employee",Annual_Income)

