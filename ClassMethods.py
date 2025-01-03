class Mobile:
    @classmethod                        #Decorator
    def show_model(cls):                #class Method
        print("Realme X")
realme=Mobile()
Mobile.show_model()                     #calling Class Method

#
class Mobile:
    fp='yes'
    @classmethod
    def show_model(cls):
        print("Fingerprint Scanner:",cls.fp)
realme=Mobile()
Mobile.show_model()