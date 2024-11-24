"""
Counter is a dictionary subclass that allows key => value mapping 
of key => int_count i.e., counter = {"aKey": 12, "bKey": 30}

c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)  
"""
from collections import Counter

countDict = Counter()


list = ["A", "A", "B", "C", "A", "D", "E", "B"]

for item in list:
    countDict[item] += 1
    
print("counter dictionary", countDict)
print("missing element", countDict["Missing"]) 

# notable functions
print("flatten elements according to their count", countDict.elements())
print("prints most common n item", countDict.most_common(2))
#total
print("totalling of", countDict.total())
      
#subtract(iterable or mapping or Counter)
countDict.subtract({"A":1, "D": 0}
print("subtracting count", countDict))


#update(iterable or maping or Counter)
countDict.update({"D": 1, "E": 1})
print("after updating", countDict)
#fromkeys(iterable) is not implemented
