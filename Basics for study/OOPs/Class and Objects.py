print("###################  Class and Objects  ###################")
print()
print()
print("1.")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print()
print("2.")
print()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

print()
print("3.")
print()


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()

print()
print()
print("###########################################################################")
print("  from another tutorial   ")
print("###########################################################################")
print()
print()


class Computer:
    def config(self):
        print("i5, 16gb, 1Tb")


comp1 = Computer()
comp2 = Computer()
b = 10
a = "Hello"

# print types
print(type(b))
print(type(a))
print(type(comp1))

# call the method within Computer class
comp1.config()      # it can also be called as Computer.config(comp1)
Computer.config(comp2)      # it can also be called as comp2.config()