class Mobile:
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
def Phone_Details(self):
    print("Phone Brand :",self.brand)
    print("Phone Color :",self.color)
    print("Phone Price :",self.price)
Phn1=Mobile("Redmi","Red",12000)
Phn2=Mobile("Realme","Blue",15000)
Phn3=Mobile("Samsung","Silver",20000)
Phn4=Mobile("OnePlus","SeaBlue",10000)
Phn5=Mobile("Google","Black",19000)
Phone_Details(Phn1)
print("-------------------------------")
Phone_Details(Phn2)
print("-------------------------------")
Phone_Details(Phn3)
print("-------------------------------")
Phone_Details(Phn4)
print("-------------------------------")
Phone_Details(Phn5)