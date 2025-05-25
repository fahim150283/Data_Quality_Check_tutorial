thislist = ["apple", "banana", "cherry", "apple", "cherry", "mango"]
print("1.",)
for x in thislist:
  print("\t",x)

thislist = ["apple", "banana", "cherry"]
print("2.",)
for i in range(len(thislist)):
  print("\t",thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
print("3.",)
while i < len(thislist):
  print("\t",thislist[i])
  i = i + 1


thislist = ["apple", "banana", "cherry"]
print("4.",)
[print("\t",x) for x in thislist]