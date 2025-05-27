print("1.")
i = 1
while i < 6:
  print("\t",i)
  i += 1


print("2.")
i = 1
while i < 6:
  print("\t",i)
  if i == 3:
    break
  i += 1




print("3.")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print("\t",x)



print("4.")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print("\t",x)



print("5.")
for x in range(6):
  print("\t",x)
else:
  print("\t","Finally finished!")



print("6.")
for x in range(6):
  if x == 3: break
  print("\t",x)
else:
  print("\t","Finally finished!")




print("7.")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print("\t",x, y)