"""
    to illustrate the order effect when applying mutliple decorator 
"""

def wrap_star(func):
    def inner(*pargs, **kargs):
        print("*" * 8)
        func(*pargs, **kargs)
        print("*" * 8)
    return inner

def wrap_percent(func):
    def inner(*pargs, **kargs):
        print("%" * 8)
        func(*pargs, **kargs)
        print("%" * 8)
    return inner

@wrap_star # will receive wrap_percent and wrap_percent will receive hero_exec
@wrap_percent
def hero_exe(*pargs, **kargs):
    hero, msg = kargs.values()
    print(f"{hero} has said: {msg}")
    
hero_exe(hero="Super man", msg=" I am born to fuck them all")

    


def smart_divide(divide_func):
    def inner(a, b):
        if b == 0:
            print("divisor can not be zero")
            return
        return divide_func(a, b)
    return inner

def describe(divide_func):
    def inner(a, b):
        result = divide_func(a, b)
        print(f"#math dividing {a} by squire of {b} result is: {result}")
    return inner


@describe
@smart_divide
def squire_divide(a, b):
    print("=> I m dividing func")
    return a / (b**2)

#squire_devide(16, 4)
squire_divide(16, 4) 
 