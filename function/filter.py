#filter(func_checkedBoolean, list | )

dataItems = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13)

result = filter(lambda x: x % 2 == 0, dataItems)

print("result is class filter?:", type(result))  # true
print("List reuslt: ", list(result))
