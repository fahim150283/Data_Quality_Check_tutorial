x = lambda a : a + 10
print("1.",x(5))


x = lambda a, b : a * b
print("2.",x(5, 6))


x = lambda a, b, c : a + b + c
print("3.",x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print("4.",mydoubler(11))



def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print("5.",mytripler(11))


def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print("6.",mydoubler(11))
print("7.",mytripler(11))