""" Tuple can be declared with (a, b, c), but enclosing brackets are optional"""
aTuple = 10, 20 , 30
print(aTuple)

nestedTuple = aTuple, 40, 50, (60, 70, 80)
print(nestedTuple)

# tuples are immutable and heterogeneous
# accessed by unpacking or indexing
# construction of tuple with 0 or 1 element require quarks

singleTuple = ("hello", 4,)
print(singleTuple)

singleTuple = "hello", 5,
print(singleTuple)
