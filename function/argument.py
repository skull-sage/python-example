def func(name, age):
  print(name, " is ", age, "years old")
  pass


func(20, 'Monkey')  # positional mapping
func(name='Sage', age=30)  # name mapping

#positional is in tuple format
def positonalVarArg(*arg):
  print(arg)
  print(arg[0])
  pass

# keyword arg is dictionary format
def keywordVarArg(**karg):
  print(karg)
  print(karg['name'])
  print(karg['behaviour'])
  pass

positonalVarArg("Rashed", 20, "Bad boy")
keywordVarArg(name = "Rashed", age = "20", behaviour = "Bad boy")


print("\n => Bounded and Unbounded test\n")
