"""
    in and not in 
    is generally for membership checking
    be cautious when membership checking of empty string: it will always return true 

"""

print( 5 in {1, 2, 5}) # True
print( 5 in (1, 2, 5)) # True
print( 5 in [1, 2, 5]) # True
print("" in "abcd") # always True

print( 5 in {1, 2, 6}) # False


