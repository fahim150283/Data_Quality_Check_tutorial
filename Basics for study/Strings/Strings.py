import multiprocessing.managers

print("###################  Strings  ###################")
print()
print()


x = "hello world"
print("1.",x)

print ()

x = "He is called 'Johnny'"
print("2.",x)

print ()

x = 'He is called "Johnny"'
print("3.",x)

print ()

x = "He is called \"Johnny\""
print("4.",x)

print ()

x = "He is called \n\"Johnny\""
print("5.",x)

print ()

x = "He is called \t\"Johnny\""
print("6.",x)




print()
print()
print()
print("###################  Multiline Strings  ###################")
print()
print()
print()

a = """I eat Rice,
He eats rice,
She drinks white juice
I am happy."""
print(a)


print()
print()

a = '''
I eat Rice,
He eats rice,
She drinks white juice
'''

print(a)


print()
print()
print()
print("###################  String Indexing  ###################")
print()
print()
print()

a = "Hello, World!"
print("1. output of a[1] is: ",a[1]," --> Where a is 'Hello, World!'")
print("1. output of a[7] is: ",a[7]," --> Where a is 'Hello, World!'")


print()

a = "Hello, World!"
print("2. output of a[2:5] is: ",a[2:5]," --> Where a is 'Hello, World!'")

print()

a = "Hello, World!"
print("3. output of a[:5] is: ",a[:5]," --> Where a is 'Hello, World!'")

print()

a = "Hello, World!"
print("4. output of a[2:] is: ",a[2:]," --> Where a is 'Hello, World!'")


print()
print("###################  Loop Through a String  ###################")
print()

a = "Hello, World!"
for x in a:
    print(x)


print()
print("###################  String Length  ###################")
print()

a = "Hello, World!"
print("Length of a is:",len(a))


print()
print("###################  Check String  ###################")
print()

a = "Hello, World!"
print("Check if 'H' is present in a:",'H' in a)

print()

a = "Hello, World!"
print("Check if 'h' is present in a:",'h' in a)

a = "Hello, World!"
if "Hell" in a:
    print("Yes, 'Hell' is present in", a)

if "help" not in a:
    print("No, 'help' is not present in", a)