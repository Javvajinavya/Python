class MarkerPen:
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
    #mutator methods
    def Set_Color(self):
        self.color='Pink'
    def Set_Price(self):
        self.price=25
    def Set_Brand(self):
        self.brand='DOMS'
    #accessor methods
    def Show_color(self):
        return self.color
    def Show_Price(self):
        return self.price
    def Shoe_Brand(self):
        return self.brand
print("Accessor methods-------------------")
m1=MarkerPen('Camelin','black',30)
Res1=m1.Shoe_Brand()
print(Res1)
res2=m1.Show_color()
print(res2)
res3=m1.Show_Price()
print(res3)
print("-----------------------------------")
m2=MarkerPen('Saino Softek','Blue',20)
Res1=m2.Shoe_Brand()
print(Res1)
res2=m2.Show_color()
print(res2)
res3=m2.Show_Price()
print(res3)
print("-----------------------------------")
m3=MarkerPen('Apasara','Red',10)
Res1=m3.Shoe_Brand()
print(Res1)
res2=m3.Show_color()
print(res2)
res3=m3.Show_Price()
print(res3)
print("-----------------------------------")
m4=MarkerPen('Nataraj','Green',20)
Res1=m4.Shoe_Brand()
print(Res1)
res2=m4.Show_color()
print(res2)
res3=m4.Show_Price()
print(res3)
print("----------------------------------------")
print("Mutator method-----------------")
m1.Set_Color()
m1.Set_Brand()
m1.Set_Price()
Res1=m1.Shoe_Brand()
print(Res1)
res2=m1.Show_color()
print(res2)
res3=m1.Show_Price()
print(res3)