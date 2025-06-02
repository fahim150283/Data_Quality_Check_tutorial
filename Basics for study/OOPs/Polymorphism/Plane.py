import Vehicle as vehicle

class Plane(vehicle):
    def drive(self):
        print("The ",self.vehicleType," is flying. Which is a ",self.year," ",self.make," ",self.model)


    def fly(self):
        print("Plane is flying")