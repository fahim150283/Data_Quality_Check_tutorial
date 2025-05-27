thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print("1.",x)
x = thisdict.get("model")
print("2.",x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print("3.",x) #before the change
car["color"] = "white"
print("4.",x) #after the change
x = thisdict.values()
print("5.",x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print("6.",x) #before the change
car["year"] = 2020
print("7.",x) #after the change


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print("8.",x) #before the change
car["color"] = "red"
print("9.",x) #after the change
x = thisdict.items()
print("10.",x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("11.","Yes, 'model' is one of the keys in the thisdict dictionary")