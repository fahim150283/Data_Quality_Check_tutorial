class Animal:
    def alive(self):
        print("Animal is alive")

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("Rabbit is running")

class Fish(Animal):
    def swim(self):
        print("Fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("Hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()

rabbit.alive()
fish.alive()
hawk.alive()

rabbit.eat()
fish.eat()
hawk.eat()

rabbit.sleep()
fish.sleep()
hawk.sleep()