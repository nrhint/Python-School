##Nathan Hinton
##This will give the x and y distance between points

def getXAndYDistance(xi1, yi1, x2=None, y2=None):
    if x2 == y2 == None:
        x1, y1 = xi1
        x2, y2 = yi1
    else:
        x1 = xi1
        y1 = yi1
    xDist = abs(x1-x2)
    yDist = abs(y1-y2)
    return (xDist, yDist)
##Format:
##( x distance,   y distance   )
##( [int, float], [int, float] )
