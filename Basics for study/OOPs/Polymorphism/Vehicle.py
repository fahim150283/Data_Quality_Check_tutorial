class Vehicle:
    def __init__(self, make, model, year):
        vehicleType = "Vehicle"
        self.make = make
        self.model = model
        self.year = year


    def move(self):
        print("Drive!")