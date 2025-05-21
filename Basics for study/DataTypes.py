# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x = 5
print(type(x) , "--->when X = 5")

x = "Hello World"
print(type(x), "--->when X = 'Hello World'")

x = 20.5
print(type(x), "--->when X = 20.5")

x = 1j
print(type(x), "--->When X = 1j")

x = ["apple", "banana", "cherry"]
print(type(x), "--->When X ='['apple', 'banana', 'cherry']'")

x = ("apple", "banana", "cherry")
print(type(x), "--->When X = ('apple', 'banana', 'cherry')")

x = range(6)
print(type(x), "--->When X = range(6)")

x = {"name" : "John", "age" : 36}
print(type(x), "--->When X = {'name' : 'John', 'age' : 36}")

x = {"apple", "banana", "cherry"}
print(type(x), "--->When X = {'apple', 'banana', 'cherry'}")

x = frozenset({"apple", "banana", "cherry"})
print(type(x), "--->When X = frozenset({'apple', 'banana', 'cherry'})")

x = True
print(type(x), "--->When X = True")

x = b"Hello"
print(type(x), "--->When X = b'Hello'")

x = bytearray(5)
print(type(x), "--->When X = bytearray(5)")

x = memoryview(bytes(5))
print(type(x), "--->When X = memoryview(bytes(5))")

x = None
print(type(x), "--->When X = None")

