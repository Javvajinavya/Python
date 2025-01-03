class Engineer:
    def Work(self):
        print("Engineer is working")
class SoftwareEngineer(Engineer):
    def Work(self):
        print("Software engineer is working")
class CivilEngineer(Engineer):
    def Work(self):
        print("Civil Engineer is working")
E1=Engineer()
E1.Work()
Se1=SoftwareEngineer()
Se1.Work()
Ee1=CivilEngineer()
Ee1.Work()    