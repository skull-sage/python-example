"""
Decorator:
 - accept a function and decorate a logic around it with inner
 - inner decorating function should have same number of argument as the target function
 - multiple decorating function can be applied
 - decoration logic will be applied in the order assigned to target function
"""

import time        

def calc_performance(computing_func):
    def time_wrap():
        start = time.time()
        result = computing_func()
        end = time.time()
        return result, start, end 
    
    return time_wrap


def undecorated_computing():
    for idx in range(0, 50000000):
        continue
    
    return "Undecorated Computing"

ugly_performer = calc_performance(undecorated_computing)
(result, start, end) = ugly_performer()
print(f"Undecorated func {result} took: {end - start}")

@calc_performance
def decorated_computing():
    for idx in range(0, 50000000):
        continue
    
    return "Decorated Computing"

(result, start, end) = decorated_computing()
print(f"Magic decoration: {result} took: {end - start}")



