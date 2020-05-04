##Nathan Hinton
##This will return if the shape is a triangle.

from getSlopeAndLengthFromPoints import *

def arePointsTriangle(a, b, c):
    l1 = getSlopeAndLengthFromPoints(a, b)
    l2 = getSlopeAndLengthFromPoints(b, c)
    l3 = getSlopeAndLengthFromPoints(c, a)
    s1 = l1[0]
    s2 = l2[0]
    s3 = l3[0]
    slopes = [s1, s2, s3]
    for slope in slopes:
        tmp = Fraction(slope.denominator, -slope.numerator)
        if tmp in slopes:
            return True
    return False
## ( if it is )
## ( [bool] )

a, b, c = ((2, 0), (-6, 10), (-10, 4))
