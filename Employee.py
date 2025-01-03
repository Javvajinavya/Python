class Employee:
    def __init__(self,name,ID,Designation,Salary,Location,SpecailAlowances):
        self.name=name
        self.ID=ID
        self.Designation=Designation
        self.Salary=Salary
        self.Location=Location
        self.Allowances=SpecailAlowances
Emp1=Employee("Roy",101,"Engineer",12000,"Hyderabd","Travel Allowances")
print("Employee Name:",Emp1.name)
print("Employee Id: ",Emp1.ID)
print("Employee Designation :",Emp1.Designation)
print("Employee Salary",Emp1.Salary)
print("Employee Location :",Emp1.Location)
print("Employee Special Allowances :",Emp1.Allowances)
Emp2=Employee("John",102,"Developer",14000,"Vijayawada","food Allowances")
print("Employee Name:",Emp2.name)
print("Employee Id: ",Emp2.ID)
print("Employee Designation :",Emp2.Designation)
print("Employee Salary",Emp2.Salary)
print("Employee Location :",Emp2.Location)
print("Employee Special Allowances :",Emp2.Allowances)
Emp3=Employee("Rickey",103,"Tester",14000,"Chennai","living Allowanced")
print("Employee Name:",Emp3.name)
print("Employee Id: ",Emp3.ID)
print("Employee Designation :",Emp3.Designation)
print("Employee Salary",Emp3.Salary)
print("Employee Location :",Emp3.Location)
print("Employee Special Allowances :",Emp3.Allowances)
