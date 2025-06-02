import Vehicle as vehicle

class Boat(vehicle):
    def __init__(self, make, model, year):
        self.vehicleType = "Boat"
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("The ",self.vehicleType," is Riding. Which is a ",self.year," ",self.make," ",self.model)