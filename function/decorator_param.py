"""
    To make a decorator to have parameter  we need to transform a 
    decorator(func, args) => wrapped_decorator(func) with  decorator_wrapping technique
    
"""

def parameterized(decorator_func):
    def wrapper_for_arg(*args, **kargs):
        return lambda func : decorator_func(func, *args, **kargs)
    return wrapper_for_arg

        
@parameterized
def result_multiply(func, num):
    def wrapper(*args, **kargs):
        result = num * func(*args, **kargs)
        return result
    pass

    return wrapper

@result_multiply(5)
def geometricFunc(x, c):
    return x + c


print(geometricFunc(5, 2))


