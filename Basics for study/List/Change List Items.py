thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print("1.",thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print("2.",thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print("3.",thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print("4.",thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print("5.",thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print("6.",thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print("7.",thislist)

thislist1 = ["apple", "banana", "cherry"]
thislist2 = ["orange", "mango", "grapes"]
thislist1.extend(thislist2)
print("8.",thislist1)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print("9.",thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print("10.",thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print("11.",thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("12.",thislist)