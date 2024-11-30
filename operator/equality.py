"""
    In Python,
    we use == for value equality
    and is for reference equality
"""

def checkEquality(**kargs):
    key_tuples = tuple(kargs.keys())
    val_tuples = tuple(kargs.values())
    print(f"{key_tuples[0]} == {key_tuples[1]}? {val_tuples[0] == val_tuples[1]}")
    print(f"{key_tuples[0]} is {key_tuples[1]}? {val_tuples[0] is val_tuples[1]} \n")
    


checkEquality(numbX=5, numbY=5) 
checkEquality(strX="Hello", strY="Hello")
checkEquality(tupleX=(1, 2, 3), tupleY=(1, 2, 3))
checkEquality(listX=[1, 2, 3], listY=[1, 2, 3])

 
 


