class Watch:
    @staticmethod
    def ShowTime():
        print("Watch shows time ...........")
    @classmethod
    def ShowBrand(self):
        print("Watch brand is Rolex......")
    def __init__(self,color):
        print("Object is created")
        self.color=color
    def Get_Color(self):
        print(self.color)
w1=Watch('Silver')
Watch.ShowTime()
Watch.ShowBrand()
w1.Get_Color()
w1.ShowTime()