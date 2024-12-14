"""
    cache - cache a function computation for specific argument
"""

from functools import cache

@cache
def rangeSquireSum(len):
    total = 0;
    print("# Not cached! Computing for: ", len)
    for idx in range(1, len+1):
        total = total + idx ** 2
        continue
    
    return total

print("squire sum of range: 1 is ", rangeSquireSum(1))
print("squire sum of range 2 is ", rangeSquireSum(2))
print("squire sum of range: 3 is", rangeSquireSum(3))
print("squire sum of range 2 is ", rangeSquireSum(2))


# we can use cache_info() on function object to get an statistics
print(rangeSquireSum.cache_info())