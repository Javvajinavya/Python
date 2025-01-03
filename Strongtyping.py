class Duck:
    def Walk(self):
        print("thapak thapak thapak thapak")
class Horse:
    def Walk(self):
        print("tabdak tabdak tabdak tabdak")
class Cat:
    def talk(self):
        print("Meow Meow")
def myfunction(obj):
    if hasattr(obj, 'walk'):
        obj.walk()
    if hasattr(obj, 'walk'):
        obj.talk()
d=Duck()
myfunction(d)
h=Horse
myfunction(h)
c=Cat()
myfunction(c)