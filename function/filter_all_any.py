#filter(predicate, iterable)

dataItems = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13)

result = filter(lambda x: x % 2 == 0, dataItems)

print("result is class filter?:", type(result))  # true
print("List reuslt: ", list(result))


# all(iterable) returns True if all items are truthy
# in python, falsy values are: False, [], '', None

result = all([True, 'String', 1, 2.56, []])
print(result)

# any(iterable) returns True if any truthy value found
result = any([False, [], '', True])
print(result)

