thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("1.",thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print("2.",thisdict)
print("3.",len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print("4.",thisdict)
print("5.",type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print("6.",thisdict)


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print("7.")
for x in thisdict:
  print("\t",x)
print("8.")
for x in thisdict:
  print("\t",thisdict[x])


print("9.")
for x in thisdict.values():
  print("\t",x)


print("10.")
for x in thisdict.keys():
  print("\t",x)


print("11.")
for x in thisdict.items():
  print("\t",x)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print("12.",mydict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print("13.",mydict)