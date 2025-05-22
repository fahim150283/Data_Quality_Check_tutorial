print()
print("################## For Positive ##################")
print()


x = 3
y = 4j
z = 5.01

print(type(x), "--> When x = 3")
print(type(y), "--> When y = 4j")
print(type(z), "--> When z = 5.01")

print()
print("################## For Negative ##################")
print()

x = -3
y = -4j
z = -5.01

print(type(x), "--> When x = -3")
print(type(y), "--> When y = -4j")
print(type(z), "--> When z = -5.01")

print()
print("################## Type Conversion ##################")
print()

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(type(a),"--> When a = ",a)
print(type(b),"--> When b = ",b)
print(type(c),"--> When c = ",c)


import random
print("Random Number = ",random.randrange(1,10))