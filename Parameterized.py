#paramterized constructor
class Student:
    def __init__(self,name,age):
        print("Object is created")
        self.name=name
        self.age=age
Std1=Student("Maggie",20)
print("Student name is:",Std1.name)
print("Student age is :",Std1.age)
Std2=Student("Navya",20)
print("Student name is:",Std2.name)
print("Student age is :",Std2.age)