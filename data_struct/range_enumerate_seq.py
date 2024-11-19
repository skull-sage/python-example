def enumerateEx():
  item_list = ['apple', 'orange', 'banana']
  enumtd = enumerate(item_list)

  print("item in enumerate is tuple?:", type(next(enumtd)) )

  # to access as list we must listify it: list(enumtd)
  print(list(enumtd))
  pass


def filterExm():
  """
    filter(predicate, iterable) return a filter class. 
    We must listify it to get the result
  """
  item_list = ['apple', 'orange', 'banana', 'apple', 'orange']
  fltList = filter(lambda x: x == 'apple', item_list)
  print("filtered: ", type(fltList))

# enumerateEx()
filterExm()

