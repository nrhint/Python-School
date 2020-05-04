##Nathan Hinton
##This will return a point with a given ratio between 2 points

from getXAndYDistance import getXAndYDistance
from getSlopeAndLengthFromPoints import getSlopeAndLengthFromPoints
from fractions import Fraction

def getRatioBetweenTwoPoints(ratio, xi1, yi1):
    xDist, yDist = getXAndYDistance(xi1, yi1)
    d = getSlopeAndLengthFromPoints(xi1, yi1)
    try:
        ratio = Fraction(ratio)
    except ValueError:
        print("ERROR converting the ratio into a fraction.")
        print("This should be done in the format '2/3'")
##    xStep = xDist/ratio.denominator
##    yStep = yDist/ratio.denominator
    x = xDist * ratio #xStep*ratio.numerator
    y = yDist * ratio #yStep*ratio.numerator
    if d[0] < 0: #If it is a negative slope:
        return (xi1[0] + x, xi1[1] - y)
    else:
        return (xi1[0] + x, xi1[1] + y)
##Returns a point that is a ratio along a line
##(     x,            y        )
##( [int, float], [int, float] )
