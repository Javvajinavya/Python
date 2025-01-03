class Employee:
    def __init__(self,name,ID,Designation,Salary,Location,SpecailAlowances):
        self.name=name
        self.ID=ID
        self.Designation=Designation
        self.Salary=Salary
        self.Location=Location
        self.Allowances=SpecailAlowances
        print("Employee Name:",self.name)
        print("Employee Id: ",self.ID)
        print("Employee Designation :",self.Designation)
        print("Employee Salary",self.Salary)
        print("Employee Location :",self.Location)
        print("Employee Special Allowances :",self.Allowances)
Emp1=Employee("Roy",101,"Engineer",12000,"Hyderabd","Travel Allowances")
