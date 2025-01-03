'''#Duck class
class Duck:
    def walk(self):
        print("thapak thapak thapak thapak ")
#Hotse class
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")
def myfunction(obj):
    obj.walk()
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)'''



class Father:
    def Work(self):
        print("Hard working father")
class Son:
    def Work(self):
        print("Enjoying son ")
def Result(self):
    self.work()
F1=Father()
Result(F1)
S2=Son()
Result(S2)