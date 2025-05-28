def func1(fname):
  print("\t" + fname)

def func2(fname, lname):
  print("\t" + fname + " " + lname)

def func3(*kids):
  print("\t","The youngest child is " + kids[len(kids)-1])
  print("\t","The oldest child is " + kids[0])
  print("\t","The middle child is " + kids[len(kids)//2])

def func4(country ="Norway"):
  print("\t","I am from " + country)

def func5(fruits):
  for x in fruits:
    print("\t",x)

print("1.")
(func2("Will", "Smith"))

print("2.")
func1("Emil")
func1("Tobias")
func1("Linus")


print("3.")
func3("Emil", "Tobias", "Linus", "Will", "Smith")


print("4.")
func4("Sweden")
func4("India")
func4()
func4("Brazil")


print("5.")
fruits = ["apple", "banana", "cherry"]
func5(fruits)




print("6. Recursion")
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print("\t",result)
  else:
    result = 0
  return result
tri_recursion(6)