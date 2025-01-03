class Mobile:
    def __init__(self):
        print("Object is created")
        self.price=10000
    def show_model(self,price):
        print(self.price)
Samsung=Mobile()
Samsung.show_model(1000)

class MarkerPen:
    def __Init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
    def Show_color(self):
        return self.color
    def Show_Price(self):
        return self.price
    def Shoe_Brand(self):
        return self.brand
m1=MarkerPen('Camelin','black',30)
Res1=m1.Shoe_Brand()
print(Res1)
res2=m1.Show_color()
print(res2)
res3=m1.Show_Price()
print(res3)
m2=MarkerPen('Saino Softek','Blue',20)
Res1=m2.Shoe_Brand()
print(Res1)
res2=m2.Show_color()
print(res2)
res3=m2.Show_Price()
print(res3)
m3=MarkerPen('Apasara','Red',10)
Res1=m3.Shoe_Brand()
print(Res1)
res2=m3.Show_color()
print(res2)
res3=m3.Show_Price()
print(res3)
m4=MarkerPen('Nataraj','Green',20)
Res1=m4.Shoe_Brand()
print(Res1)
res2=m4.Show_color()
print(res2)
res3=m4.Show_Price()
print(res3)