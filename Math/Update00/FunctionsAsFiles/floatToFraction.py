##Nathan Hinton

from fractions import Fraction

def floatToFraction(f):
    frac = Fraction(f)
    print(frac.numerator +"/"+frac.denominator)
    return frac
