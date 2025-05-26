# Sort List Alphanumerically

mylist = ["banana", "cherry","kiwi", "apple", "mango"]
mylist.sort()
print("1.",mylist)


mylist = ["banana", "cherry","kiwi", "apple", "mango"]
mylist.sort(reverse = True)
print("2.",mylist)


mylist = [5,10,13,8,7]
mylist.sort()
print("3.",mylist)


mylist = [5,10,13,8,7]
mylist.sort(reverse = True)
print("4.",mylist)


# Customize Sort Function

def myfunc(n):
    return abs(n - 50)

mylist = [100, 50, 65, 82, 23,49,52]
mylist.sort(key = myfunc)
print("5.",mylist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)