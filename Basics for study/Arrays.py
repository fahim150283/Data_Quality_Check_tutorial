cars = ["Ford", "Volvo", "BMW", "Mercedes"]
print("1.", cars[0])

cars[0] = "Toyota"
print("2.", cars[0])

x = len(cars)
print("3.", x)

for x in cars:
    print(x)

cars.append("Honda")
print("4.", cars)

cars.pop(1)
print("5.", cars)

cars.remove("BMW")
print("6.", cars)

cars.sort()
print("7.", cars)

cars.sort(reverse=True)
print("8.", cars)

cars.clear()
print("9.", cars)

cars = ["Ford", "Volvo", "BMW", "Mercedes", "BMW"]
alist = cars.copy()
print("10.", alist)

print("11.", cars.count("BMW"))

print("13.", cars.index("BMW", 3))

print("14.", cars.index("Mercedes"))

cars.insert(1, "Honda")
print("15.", cars)

cars.reverse()
print("16.", cars)