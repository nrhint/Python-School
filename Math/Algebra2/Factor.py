##Nathan Hinton
##This program will factor a number.
##I plan to use it for factoring radicals
##See https://codereview.stackexchange.com/questions/144041/reduce-square-root-to-simplest-radical-form
##For source/reference
print("Initalizing Factor.py")
from math import sqrt

def reduced_sqrt(n):
    n = int(n)
    try:
        root = int(sqrt(n))
    except ValueError:
        root = int(sqrt(n*-1))
    for factor_root in range(root, 1, -1):
        factor = factor_root * factor_root
        if n % factor == 0:
            reduced = n // factor
            return (factor_root, reduced)
    return (1, n)

def print_reduced_sqrt(n):
    n = int(n)
    coefficient, reduced = reduced_sqrt(n)
    if coefficient == 1:
        print('\u221A', reduced)
    elif reduced == 1:
        print(coefficient)
    else:
        print(coefficient, '\u221A', reduced)
