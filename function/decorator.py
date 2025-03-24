"""
Decorator:
 - accept a function and decorate a logic around it with inner
 - inner decorating function should have same number of argument as the target function
 - multiple decorating function can be applied
 - decoration logic will be applied in the order assigned to target function
"""

import time        

def track_performance(computing_func):
    def time_wrap(*pargs, **kargs):
        start = time.time()
        result = computing_func(*pargs, *kargs)
        end = time.time()
        
        print(f"{computing_func.__name__} took: {end - start}")
        
        return result, start, end 
    
    return time_wrap


def undecorated_computing(count_len):
    for idx in range(0, count_len):
        continue
    
    return "Unsmart Work"

ugly_performer = track_performance(undecorated_computing)
(result, start, end) = ugly_performer(4000000) 
print(f"Without decoration,  Returned Result is #{result}  ")

@track_performance
def decorated_computing(count_len):
    for idx in range(0, count_len):
        continue
    
    return "Smart Work"

(result, start, end) = decorated_computing(50000000)
print(f"Magic decoration, Returned Result is #{result}  ")



