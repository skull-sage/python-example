# genItem is actually a generator object which is iterable


# Generator build iterator with ( expression )
genItem = (x * 2 for x in range(5))
print(genItem)
print(next(genItem))


def genEven():
  for x in range(1, 10):
    if x % 2 == 0:
      yield x
  pass

# invoking genEven return an instance
genEvenItem = genEven()



print(genEven) # prints type <function genEven 0xaddress>
print(genEvenItem) # prints type <generator object genEven 0xaddress>

# print(list(genEvenItem))
for idx, item in enumerate(genEvenItem, 1):
    print(idx, item)
    

# we cans send data to generator to process
print("### Lets send data to an accumulator")

def accumulator():
  total = 0
  while True:
     value = yield total
     total = total + value
     continue
  pass

acc = accumulator()
#lets start the generator first
next(acc)
print(acc.send(20))
print(acc.send(30))
print(acc.send(40))

