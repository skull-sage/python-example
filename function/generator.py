# Comprehension build list with [ expression ]
# Generator build iterator with ( expression )

genItem = (x * 2 for x in range(5))

# genItem is actually a generator object which is iterable
print(genItem)

print(next(genItem))
print(next(genItem))
# iteration start from 3rd iterable due to first 2-next call
# we can build list and tuple
# print(list(genItem))
print(tuple(genItem))


def genEven():
  for x in range(1, 10):
    if x % 2 == 0:
      yield x * 2
  pass

genEvenItem = genEven()

print(genEven) # prints type <function genEven 0xaddress>
print(genEvenItem) # prints type <generator object genEven 0xaddress>

# print(list(genEvenItem))
for idx, item in enumerate(genEvenItem, 1):
    print(idx, item)
    
