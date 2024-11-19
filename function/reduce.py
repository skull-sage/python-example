# reduce(func_to_combine_item_of_iterables, iterables)
# func has two arguments first one is last result, second one is next item
# it scan item from left to right, applies result from prev scan to next

itemList = {1, 2, 3, 4}

result = reduce(lambda x, y: x + y *2, itemList)