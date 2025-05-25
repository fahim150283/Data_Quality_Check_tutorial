fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print("1.",newlist)




fruits = ["apple", "guava", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print("2.",newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print("3.",newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x not in ("apple", "banana", "cherry")]
print("4.",newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in range(5)]
print("5.",newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in range(10) if x < 5]
print("6.",newlist)