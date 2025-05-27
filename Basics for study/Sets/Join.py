"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print("1.",set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print("2.",set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 | set4
print("3.",myset)

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print("4.",z)

x = {"a", "b", "c"}
y = (1, 2, 3)
x.update(y)
print("5.",x)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "b", "c"}
myset = set1.intersection(set2)
print("6.",myset)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print("7.",set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print("8.",set1)

set1 = {"apple", "banana", "cherry", "peach"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print("9.",set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print("10.",set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print("11.",set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print("12.",set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2    # The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
print("13.",set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print("14.",set1)