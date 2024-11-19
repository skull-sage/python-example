from math import log
from sympy import *

def tryLog(n, base = None):
  if(base is None) :
    """with out base log(n) means log(n, e) ~ ln(n)"""
    x = log(n) 
    print(f"natural log of {n} is {x.evalf()}")
  else:
    x = log(n, base)
  print(f"log of {n, base} is {x}")
  pass


# tryLog(10);
# tryLog(10, 10);


def tryLimit():
  x = symbols('x')
  f = 1/x
  result = limit(f, x, oo)
  print(result)
  pass

def tryExponentFunc():
  n = symbols('n')
  f = (1 + 1/n)**n
  result = limit(f, n, oo)
  print(result)
  print(result.evalf())
  pass


def tryDerivative():
  x = symbols('x')
  f = x**2
  drvX = diff(f, x)
  print(f"derivative is: {drvX}")
  print(f"and derivative(slope) at x=2 is {drvX.subs(x, 2)}")
  pass


def tryDerivativeWithSlop():
  x, s = symbols('x s')
  f = x**2
  slope_f = (f.subs(x, x + s) - f) / ((x + s) - x)
  slope_at_2 = slope_f.subs(x, 2)
  print("slope at 2", slope_at_2)
  
  result = limit(slope_at_2, s, 0)
  print("Finally limiting s->0 ", result)
  pass

def tryChainRule():
  x, y = symbols('x y')
  y = x**2 + 1
  z = y**3 - 2
  dz_dx = diff(z, x)
  print("dz/dx = ", dz_dx)


def tryIntegral():
  x = symbols('x')
  f = x ** 2
  indF = integrate(f, x) # indefinite
  dF = integrate(f, (x, 0, 2)) # definite
  print(f"indefinite integration is: {indF}")
  print(f"definite integration is: {dF}")
  pass

  
def tryIntegralExample():
  x = symbols('x')
  f = 3*(x ** 2) + 1
  dfIntgral = integrate(f, (x, 0, 2))
  print(f"df Integral is: {dfIntgral}")
  pass

tryIntegralExample();
  