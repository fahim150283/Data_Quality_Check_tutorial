thisset = {"apple", "banana", "cherry"}
print("1.",thisset)

thisset = {"apple", "banana", "cherry", "apple", "cherry"}
print("2.",thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print("3.",thisset)

thisset = {"apple", "banana", "cherry",1, 2, False, True, 0}
print("4.",thisset)

print("5.",len(thisset))

print("6.",type(thisset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print("7.",thisset)

print()
print()
print("################################# Access Set Items #################################")
print()
print()

thisset = {"apple", "banana", "cherry"}
print("1.")
for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("2.","banana" in thisset)

thisset = {"apple", "banana", "cherry"}
print("3.","banana" not in thisset)