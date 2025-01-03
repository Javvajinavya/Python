class Vehicle:
    def __init__(self):
        print("Vehicle class constrcutor")
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        print("Bike Class Constructor")
class SuperBike(Bike):
    def __init__(self):
        super().__init__()
        print("Super Bike class Constrcutor")
S1=SuperBike()