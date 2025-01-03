#Instance Variable with Instance Method
class Mobile:
    def __init__(self):
        self.model='Realme X'
    def show_model(self):
        print(self.model)
realme=Mobile()
realme.show_model()
#Accessing Instance Variable from Outside Class
r=realme.model
print("Outside Class: ", r)