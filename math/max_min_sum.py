import math

list = [10, 9, 8 , 7 , 6, 5, 4, 3, 2, 1]

# finding max
print("max: ", max(list))
max_elm_divis3 = max(list, key=lambda x: x if x % 3 == 0 else -1)
print("max_divisible_3", max_elm_divis3)


print("sum of elm: ", sum(list))
print("sum of even: ", sum(list, 5))