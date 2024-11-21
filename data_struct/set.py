"""
    There is two way to create a set
    using a set() function
    using a curly braces {val1, val2} just like in algebra 
    note: {key: val} mapping declares a dictionary
    
    To Remember:
        - unordered
        - unindexed
        - mutable with update, add, difference_update
        - iterable
    
    containing item(s) can be of any immutable type: literals, string, tuple
    placing mutable type: list, dictionary will result in error

"""



setA = set([10, 20, 10, 'Rashed', 'alam',  'Kashed', 'alam'])
print(setA)

setStr = set("Rashed Alam")
print("string: ", setStr)

aVar = 'duck'
setCurly = {10, 'chicken', aVar, 'duck', 20, (10, 20, 30)}

print(setCurly)
 
"""
setWithMutable = {10, 5, {"name": "alex"}}
print(setWithMutable) # TypeError: UnHashable type: 'dict' 

"""
# checking membership
fruitA = {"apple", "orange", "mango", "jack fruit"}
print("orange" in fruitA)
print("Dragon" not in fruitA)


 
#  algebra set ops:  
print("diff (A - B)", {"a", "b"}.difference({"b", "c"}))
print("symmetric diff/delta (A Δ B)", {"a", "b"}.symmetric_difference({"b", "c"}))

print("intersection (A ∩ B)", {"a", "b"}.intersection({"b", "c"}))
print("union (A U B)", {"a", "b"}.union({"b", "c"}))
  
 
# update (update/union), difference_update, symmetric_difference_update, intersection_update allow mutation with iterable: list, tuple etc
fruitA = {"a", "b", "c"}
print(f"===starting with fruit set {fruitA}===")
fruitA.update(["c", "d", "e"])
print("updated: ", fruitA) 

fruitA.difference_update(["c", "d"])
print("diff updated:", fruitA)

fruitA.symmetric_difference_update(["b", "c", "e"])
print("symmetric diff updated:", fruitA)
 
# discard, remove
# discard & remove both takes single element as argument
# discard doesn't raise error for absent element while remove does
setA = {1, 2, 3}
setA.discard(2)
print(setA)
setA.discard(4)
print(setA)

import traceback
 

try:
    # results in error for absent element unlike discard
    # this also mean trying any element on empty set will be error
    setA.remove(4) 
except Exception:
    print(traceback.format_exc())
 

# pop evicts an element randomly 
try:
    print(setA.pop())  
    print(setA.pop())  
    print(setA.pop()) # error if set is empty
except Exception: 
    print(traceback.format_exc())

setA.clear() #will clear the set
