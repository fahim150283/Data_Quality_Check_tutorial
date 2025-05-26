thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print("1.",thistuple)
print("2.",len(thistuple))

thistuple = ("apple",)
print("3.",type(thistuple))

#NOT a tuple
thistuple = ("apple")
print("4.",type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print("5.",tuple1)
print("6.",tuple2)
print("7.",tuple3)

thistuple = ("apple", "banana", "cherry")
print("8.",len(thistuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print("9.",thistuple)