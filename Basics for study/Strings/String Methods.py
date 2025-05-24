# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning


a = "Hello, World!"
print("1.",a.capitalize())

a = "Hello, World!"
print("2.",a.casefold())

a = "Hello, World!"
print("3.",a.center(18))

a = "HelloH, World!"
print("4.",a.count("H"), "-Total 'H' in", a)

a = "Hello, World!"
b = a.encode()
print("5.")
print("5.1.",b)
b=b.decode()
print("5.2.",b)

a = "Hello, World!"
print("6.",a.endswith("d!"))

txt = "H\te\tl\tl\to"
print("7.")
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

a = "Hello, welcome to my world."
print("8.",a.find("o"))

a = "Hello, The time for that is {time:.2f}!"
print("9.",a.format(time = 3.14159))

a = "Hello, World!"
print("10.",a.index("W"))

a = "Hello, World!"
b = "HellWorld500"
print("11.1.",a.isalnum())
print("11.2.",b.isalnum())

a = "Hello, World!"
b = "HellWorld500"
print("12.1.",a.isalpha())
print("12.2.",b.isalpha())

a = "Hello, World!"
b = "101010111010"
print("13.1.",a.isascii())
print("13.2.",b.isascii())

a = "Hello, World!"
b = "101010111010"
print("14.1.",a.isdecimal())
print("14.2.",b.isdecimal())

a = "Hello, World!"
b = "1"
print("15.1.",a.isdigit())
print("15.2.",b.isdigit())

a = "Hello, World!"
print("16.",a.isidentifier())

a = "Hello, World!"
print("17.",a.islower())

a = "Hello, World!"
print("18.",a.isnumeric())

a = "Hello, World!"
print("19.",a.isprintable())

a = "Hello, World!"
print("20.",a.isspace())

a = "Hello, World!"
print("21.",a.istitle())

a = "Hello, World!"
print("22.",a.isupper())

a = "Hello, World!"
print("23.",a.join("myname"))

a = "Hello, World!"
print("24.",a.ljust(20))

a = "Hello, World!"
print("25.",a.lower())

a = "Hello, World!"
print("26.",a.lstrip())

a = "Hello, World!"
print("27.",a.maketrans("H", "J"))

a = "Hello, World!"
print("28.",a.partition("H"))

a = "Hello, World!"
print("29.",a.replace("H", "J"))

a = "Hello, World!"
print("30.",a.rfind("H"))

a = "Hello, World!"
print("31.",a.rindex("H"))

a = "Hello, World!"
print("32.",a.rjust(20))

a = "Hello, World!"
print("33.",a.rpartition("H"))

a = "Hello, World!"
print("34.",a.rsplit())

a = "Hello, World!"
print("35.",a.rstrip())

a = "Hello, World!"
print("36.",a.split())

a = "Hello, World!"
print("37.",a.splitlines())

a = "Hello, World!"
print("38.",a.startswith("H"))

a = "Hello, World!"
print("39.",a.strip())

a = "Hello, World!"
print("40.",a.swapcase())

a = "Hello, World!"
print("41.",a.title())

a = "Hello, World!"
mydict = {83:  80}
print("42.",a.translate(mydict))

a = "Hello, World!"
print("43.",a.upper())

a = "Hello, World!"
print("44.",a.zfill(20))