class Engineer:
    def __init__(self):
        print("Engineer class constrcutor")
E1=Engineer()
print("-----------------------")
class SoftwareEngineer(Engineer):
    def __init__(self):
        super().__init__()
        print("Software engineer class constructor")
S1=SoftwareEngineer()
print("-----------------------")
class CivilEngineer(Engineer):
    def __init__(self):
        super().__init__()
        print("Civil Engineer class Cointrutor")
C1=CivilEngineer()
print("-----------------------")
class MechanicalEngineer(Engineer):
    def __init__(self):
        super().__init__()
        print("Mechanical engineer")
M1=MechanicalEngineer()