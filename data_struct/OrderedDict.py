"""
    ordered dictionaries difference with dict
     - dict is good for mapping but tracking insertion order was secondary
     - OrderedDict is good with reordering ops; space, iteration and update efficiency are secondary 
     - unlike dict, equality (==) of OrderedDict checks for matching order
     - OrderedDict has move_to_end(key, last_boolean) to efficiently reposition an element to an endpoint
     - popitem(last=True)
"""

from collections import OrderedDict

ord_dict = OrderedDict.fromkeys({"A", "C", "D", "B"})
ord_dict.move_to_end('B') # last = True means last-end
print(ord_dict)
ord_dict.move_to_end('B', False) # last = False means first-end
print(ord_dict)

ord_dict.popitem() # as last element C should be popped
print(ord_dict)
ord_dict.popitem(last=False)
print(ord_dict)
