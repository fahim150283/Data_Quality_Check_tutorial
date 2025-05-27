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


print()
print()
print("###################### Unpack Tuples ######################")
print()
print()

fruits = ("apple", "banana", "cherry")

(x, y, z) = fruits

print("1.",x)
print("2.",y)
print("3.",z)


fruits = ("apple", "banana", "cherry", "strawberry", "kiwi")

(green, *yellow, red) = fruits

print("4.",green)
print("5.",yellow)
print("6.",red)


print()
print()
print("###################### Loop Tuples ######################")
print()
print()


thistuple = ("apple", "banana", "cherry")
print("1.")
for x in thistuple:
    print(x)

thistuple = ("apple", "banana", "cherry")
print("2.")
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
print("3.")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

print()
print()
print("###################### Join Tuples ######################")
print()
print()

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print("1.",tuple3)

print()

tuple1 = ("a", "b" , "c")
mytuple = tuple1 * 2
print("2.",mytuple)

print()
print()
print("###################### Tuple Methods ######################")
print()
print()

thistuple = (5,1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)
print("1.",x)

x = thistuple.index(8)
print("2.",x)