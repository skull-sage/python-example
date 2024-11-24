"""

    a key-value mapping structure
    retain order of key insertion
    allowed type for key: strings, numbers and tuples 
    
"""
print("\n=== Creating Dictionary ===")
dataMap = {"key1": "Val 1", 1: "val 2", (10, 20): "tuple (10, 20)"}
print(dataMap)

# dict function creates a map utlizing **kargs
dataMap2 = dict(key3="val 3", key1="val 1", key2="val 2")
print(dataMap2)


dataMap3 = dict([("key1", "tuple val 1"), ("key2", "tuple val 2")])
print(dataMap3)

dataMap4 = dict.fromkeys(("A", "B", "C"), (1, 2, 3))
print(dataMap4)


print("\n==== retrieving elements ===")
print("single item get(): ", dataMap.get(401, "Key Not Found")) # second arg is optional and get
print("list of item: (key, val)", dataMap.items())
print("list of keys", dataMap.keys())
print("list of values", dataMap.values())

print("\n=== dictionary modification === ")
# setdefault(key, val) will set the key to val only if key already didn't exist;
# if key already exist it will return existing value instead of changing it
dataMap.setdefault(401, "Bad Bad Request")
print(dataMap)
dataMap[404] = "Not Found :)" # for single key [string key]
dataMap.update({402: "420 Fazlami", 403: "Forbidden Atta"}) # for multiple element
print(dataMap)
print("pop from end", dataMap.popitem())
print("specific pop", dataMap.pop((10, 20)))
