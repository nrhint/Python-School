##Nathan Hinon
##This is the main program for algebra 2

print("Setting up...")
print("This uses sympy...")

import sympy as sym

print("setting up common vars...")
a = sym.symbols('a')
b = sym.symbols('b')
c = sym.symbols('c')
d = sym.symbols('d')
e = sym.symbols('e')
x = sym.symbols('x')
y = sym.symbols('y')
z = sym.symbols('z')


def solveForX(var, expr):
    for v in var:
        v = sym.symbols(str(v))

def solve(expr, term):
    print(sym.solve(expr, term))
