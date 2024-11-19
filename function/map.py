#MAP apply a function on elements from a set, list or tuple


#defining a higher order function curry
def multiplier(m):
  def multiply(num):
    return num * m
  return multiply


counters = [3, 4, 5, 6]
#this is actually a dictionary
tuple = (7, 8, 9)

#currying with map
result = map(multiplier(2), tuple)

print("result map", list(result))

# with lambda

result = map(lambda x: x * 2, counters)
print("lambda result", list(result))
