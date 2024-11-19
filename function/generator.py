# Comprehension build list with [ expression ]
# Generator build iterator with ( expression )

genItem = (x * 2 for x in range(5))

# genItem is actually a generator object which is iterable
print(genItem)

print(next(genItem))
print(next(genItem))
# iteration start from 3rd iterable due to first 2-next call
# we cab build list and tuple
# print(list(genItem))
print(tuple(genItem))


def genEven():
  d = 4
  for x in range(10):
    if d % 2 == 0:
      yield d
      d += 4
  pass

genEvenItem = genEven()
print(list(genEvenItem))

# invoking list on 26 will make generation complete
print(next(genEvenItem)) 
print(next(genEvenItem))