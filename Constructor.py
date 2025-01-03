class Student:
    def __init__(self):
        print("Object is created")
Std1=Student()
print(Std1)
Std2=Student()
print(Std2)

#nonparameterized constructor
class Student:
    def __init__(self):
        print("Object is created")
        #Direct imitialization
        self.name="Lowkika"
        self.age=21
Std1=Student()
print("Student Name:",Std1.name)
print("Age of Student:",Std1.age)
Std2=Student()
print("Student Name:",Std2.name)
print("Age of Student:",Std2.age)

