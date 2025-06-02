import Vehicle as vehicle

class Car(vehicle):

    def drive(self):
        print("The ",self.vehicleType," is driving. Which is a ",self.year," ",self.make," ",self.model)