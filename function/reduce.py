# reduce(func(accumulator, item),  iterables)
# func has two arguments first one is result accumulator, second one is next item
# reduce function needs to imported from functool 

from functools import reduce

itemList = {1, 2, 3, 4}

# reduce/fold all item to a sum
result = reduce(lambda sum, item: sum + item, itemList)
print("item summation", result)

# reduce/fold all item by multiplying all 
result = reduce(lambda prd, item: prd * item, itemList)
print("item multiplied: ", result)