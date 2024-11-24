"""
Counter is a dictionary subclass that allows key => value mapping 
of key => int_count i.e., counter = {"aKey": 12, "bKey": 30}

c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)  
"""
from collections import Counter

count_dict = Counter()


list = ["B", "C",  "D", "E", "A", "B", "A", "A"]

for item in list:
    count_dict[item] += 1
    
print("counter dictionary", count_dict)
print("missing element", count_dict["Missing"]) 

# notable functions
print("flatten elements according to their count", count_dict.elements())
print("most common n=2 item", count_dict.most_common(2))
otuple_list = count_dict.most_common()
print("item ordered as per occurance", otuple_list)
print("least occured: ", otuple_list[:-1:-1])

#total
print("totalling of", count_dict.total())

# Modification
      
#subtract(iterable or mapping or Counter)
count_dict.subtract({"A":1, "D": 2})
print("subtracting count", count_dict)
 
count_dict.update({"D": 4, "E": 5})
print("after updating", count_dict)


#fromkeys(iterable) is not implemented; Counter(iterable) can be used instead

#matchmatical operation on Counter; counter that results in 0 or less are omited from result
counter_1 = Counter(['a', 'b', 'c'])
counter_2 =  Counter({'d': 1, 'b': 2})

counter_calc = counter_1 + counter_2
print("c1 + c2", counter_calc) # d is omited

counter_calc = counter_1 - Counter(['d', 'c'])
print("c1 - c2", counter_calc)

counter_calc = counter_1 & counter_2 # intersection
print("c1 & c2", counter_calc)

counter_calc = counter_1 | counter_2 # union
print("c1 | c2", counter_calc)
