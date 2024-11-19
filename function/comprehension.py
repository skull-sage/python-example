# List comprehension collect the results of applying an arbitrary expression to an iterable of values and return them in new list
# syntax => expression for item in iterable

itemList = [ord(x) for x in 'Example']
print(itemList)

# syntax => [expression for target1 in iterable 1 if condition1
#                        for target2 in iterable 2 if condition2
#                        etc..
#           ]

# generate sum of conditional pair
itemList = [
    x + y for x in [1, 2, 3, 4] if x % 2 == 0 for y in [10, 20, 40]
    if y / 10 == x
]
print("# SUMMED LIST", itemList)

# generate list of tuple of squire
itemList = [(x, x * x) for x in [1, 2, 3, 4]]

print(itemList)
