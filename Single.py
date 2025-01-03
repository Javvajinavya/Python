class Student:
    @staticmethod
    def CollegeName():
        print("ABC College")
    @classmethod
    def writeExam(self):
        print("Enjoy Exams...")
    #Accessor method
    def ShowTime(self):
        return self.Studentname
    #Mutator method
    def Set_Name(self):
        self.Studentname='Scott'
    def __init__(self,Studentname,Id,Email):
        print("Object is created")
        self.Studentname=Studentname
        self.Id=Id
        self.Email=Email
Student.CollegeName()
Student.writeExam()
Std1=Student('Kavya',209,'kavya@email.com')
print(Std1.ShowTime())