class Parent:
    def __init__(self,a,b):
        print("Parent Constructor")
        print(a,b)

    def m1(self):
        print("Parent Method")

class Child(Parent):
    def haha(self):
        print("Child Constructor")
        super().__init__(10,20)
        super().m1()
