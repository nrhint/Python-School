##Nathan Hinton
##This will take two points and return the ength between them and the slope.

from math import sqrt
from fractions import Fraction

def getSlopeAndLengthFromPoints(xi1, yi1, x2 = None, y2 = None):
    if x2 == y2 == None:
        x1, y1 = xi1
        x2, y2 = yi1
    else:
        x1 = xi1
        y1 = yi1
    try:
        if (x2-x1) < 0:#(y2-y1) < 0 and (x2-x1) < 0:
            slope = Fraction('%s/%s'%(-(y2-y1), -(x2-x1)))
##        elif (x2-x1) < 0:
##            slope = Fraction('%s/%s'%(-(y2-y1), -(x2-x1)))
        else:
            slope = Fraction('%s/%s'%((y2-y1), (x2-x1)))
    except ZeroDivisionError:
        slope = "Undefined"
    length = sqrt(((y1-y2)**2)+((x1-x2)**2))
    lengthAsSqrt = "sqrt(%s)"%(((y1-y2)**2)+((x1-x2)**2))
    print("The slope is: y=%sx+b"%slope)
    print("The length is: %s"%length)
    return (slope, length, lengthAsSqrt)
##This will return:
##([slope as fraction], [approxLen],  [len as Sqrt])
##([Fraction],          [int, float], [str])
