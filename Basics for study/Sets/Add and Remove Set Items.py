print()
print("########## Add ##########")
print()

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print("1.",thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print("2.",thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print("3.",thisset)


print()
print()
print("########## Remove ##########")
print()
print()

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print("1.",thisset)

# Discard does not throw an error if the item to remove does not exist while Remove throws an error

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print("2.",thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print("3.",thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()   # Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
print("4.",thisset)

thisset = {"apple", "banana", "cherry"}
print("5.",thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print("6.",thisset)  # This will raise an error because the set no longer exists