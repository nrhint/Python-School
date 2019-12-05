##Nathah hinton
##this will contain all of the helper functons that I have built.

from time import sleep
from random import randint as rint
from fractions import Fraction

def EquationOfLinePassingThrough2Points(x1, y1, x2, y2):
    m = (y2-y1)/(x2/y1)
    print("slope is %s"%Fraction(m))
    

def imperialToMetric(ft, i):
    inches = (ft*12)+i
    cm = inches*2.54
    return cm
###THIS IS ALREADY BUILT INTO PYTHON UNDER THE PACKAGE "fractions"###
def fraction(i = True):
    print()
    if i == True:
        print("For division nter a double slash: \"//\"")
        i = input('Enter equation: ')
    #Begin a state machine for solving the problem:
    state = 'init'
    while state != 'end':
#        print(state)
        if state == 'init':
            if 'r' in i:
                finalTop, finalBottom = i.split('r')
                finalTop = int(finalTop)
                finalBottom = int(finalBottom)
                state = 'reduce'
            elif 'invert:' in i:
                i=i.replace('invert:', '')
                state = 'invert'
            elif '//' in i:
                state = 'divide'
            elif '*' in i:
                state = 'mult'
            elif '--' in i:
                state = 'subtract'
            elif '+' in i:
                state = 'add'
            else:
                print("fraction state machine error. No modifier found. Aborting.")
                break
        elif state == 'invert':
            top, bot = i.split('/')
            print('%s/%s'%(bot, int(top)*-1))
        elif state == 'add':
            frac1, frac2 = i.split('+')
#            print(frac1, frac2)
            top1, bottom1 = frac1.split('/')
            top2, bottom2 = frac2.split('/')
            finalBottom = int(bottom1)*int(bottom2)
            finalTop = int(top1)*int(bottom2)+int(top2)*int(bottom1)
            #reconstruct fraction:
#            print('%s/%s'%(finalTop, finalBottom))
            state = 'reduce'
        elif state == 'subtract':
            frac1, frac2 = i.split('--')
#            print(frac1, frac2)
            top1, bottom1 = frac1.split('/')
            top2, bottom2 = frac2.split('/')
            finalBottom = int(bottom1)*int(bottom2)
            finalTop = int(top1)*int(bottom2)-int(top2)*int(bottom1)
            #reconstruct fraction:
#            print('%s/%s'%(finalTop, finalBottom))
            state = 'reduce'
        elif state == 'mult':
#            print('mult')
            frac1, frac2 = i.split('*')
#            print(frac1, frac2)
            top1, bottom1 = frac1.split('/')
            top2, bottom2 = frac2.split('/')
            finalBottom = int(bottom1)*int(bottom2)
            finalTop = int(top1)*int(top2)
            #reconstruct fraction:
#            print('%s/%s'%(finalTop, finalBottom))
            state = 'reduce'
        elif state == 'divide':
            frac1, frac2 = i.split('//')
#            print(frac1, frac2)
            top1, bottom1 = frac1.split('/')
            top2, bottom2 = frac2.split('/')
            finalBottom = int(bottom1)*int(top2)
            finalTop = int(top1)*int(bottom2)
            #reconstruct fraction:
#            print('%s/%s'%(finalTop, finalBottom))
            state = 'reduce'
        elif state == 'reduce':
            changed = False
            for x in range(2, abs(finalBottom)+1):
                if finalTop%x == 0 and finalBottom%x == 0:
#                    print(x)
                    changed = True
                    finalTop = int(finalTop/x)
                    finalBottom = int(finalBottom/x)
                    break
            if changed == False:
                state = 'end'
            #state = 'end'
#        sleep(1)
    print('%s/%s'%(int(finalTop), int(finalBottom)))
    return (int(finalTop), int(finalBottom))

def slopeInterceptFormGetSlope(i = True, autoReduce = True):
    print()
    if i == True:
        print('manualInput')
        i = input()
    #Example: 10x+4y=-4
    #Step one: move the x to the correct side of the equation:
    xExpr = i[i.index('=')+1:i.index('x')+1]
##    print(xExpr)
    xMult = 0
    xMult += int(i[i.index('=')+1:i.index('x')])
##    print(xExpr, xMult)
    yExpr = i[:i.index('y')+1]
    yMult = 0
    yMult += int(i[:i.index('y')])
##    print(yExpr, yMult)
    b = int(i[i.index('x')+1:])
##    print(b)
    if autoReduce != True:
        print('slope is %s/%s'%(xMult, yMult))
        slope = '%s/%s'%(xMult, yMult)
        print('b is %x/%s'%(b, yMult))
        b = '%x/%s'%(b, yMult)
    else:
        slope = fraction(i = '%sr%s'%(xMult, yMult))
        b = fraction(i = '%sr%s'%(b, yMult))
    return '%s/%s'%(slope[0], slope[1])

def equationOfLineToSlopeInterceptForm(i = True, autoReduce = True):
    print()
    if i == True:
        print('manualInput')
        i = input()
    #Example: 10x+4y=-4
    #Step one: move the x to the correct side of the equation:
    xExpr = i[:i.index('x')+1]
    xMult = 0
    xMult += int(i[:i.index('x')])
##    print(xExpr, xMult)
    yExpr = i[i.index('x')+1:i.index('y')+1]
    yMult = 0
    yMult += int(i[i.index('x')+1:i.index('y')])
##    print(yExpr, yMult)
    b = int(i[i.index('=')+1:])
##    print(b)
    if autoReduce != True:
        print('slope is %s/%s'%(-xMult, yMult))
        slope = '%s/%s'%(-xMult, yMult)
        print('b is %x/%s'%(b, yMult))
        b = '%x/%s'%(b, yMult)
    else:
        slope = fraction(i = '%sr%s'%(-xMult, yMult))
        b = fraction(i = '%sr%s'%(b, yMult))
    return '%s/%s'%(slope[0], slope[1])

def checkForParallelOrPerpendicular(slope1, slope2):
    if slope1 == slope2:
        print("Parallel lines with a slope of %s and %s"%(slope1, slope2))
    else:
        out = fraction(i = '%s*%s'%(slope1, slope2))
        if out == (-1, 1):
            print('Perpendicular lines with a slope of %s ad %s'%(slope1, slope2))
        else:
            print('Slopes are neither Parallel or perpendicular')
    
def EQOLBTP(point1, point2):
    #m = (y2-y1)/(x2-x1)
    top = point2[1]-point1[1]
    bot = point2[0]-point1[0]
    print(top, bot)
    m = fraction(i = '%sr%s'%(top, bot))
    print('m:')
    print(m)
    #y = mx+b
    y = point2[1]
    x = point2[0]
    mx = fraction(i = '%s/%s*%s/%s'%(top, bot, x, 1))#m*x
    print('mx:')
    print(mx)
    b = fraction(i = '%s/%s--%s/%s'%(y, 1, mx[0], mx[1]))#y-mx = b
    print('b:')
    print(b)
    print('y=%s x+%s'%('%s/%s'%(m[0], m[1]), '%s/%s'%(b[0], b[1])))

def perpendicularLinePassingThroughPoint(slope, pointx, pointy):
    print('y = %s*x+b'%slope)
    print('%s = %s*%s+b'%(pointy, slope, pointx))
    x = fraction(i = '%s*%s/1'%(slope, pointx))
    print(x)
    b = fraction(i = '%s/1+%s/%s'%(pointy, -x[0], x[1]))
    print(b)

def parallelLinePassingThroughPoint(slope, pointx, pointy):
    print('y = %s*x+b'%slope)
    print('%s = %s*%s+b'%(pointy, slope, pointx))
    x = fraction(i = '%s*%s/1'%(slope, pointx))
    print(x)
    b = fraction(i = '%s/1--%s/%s'%(pointy, x[0], x[1]))
    print(b)

def compoundIntrest(start, intrestRate, time):
    for x in range(time):
        print("Year %s: %s"%(x+1, round(start*(1+intrestRate), 4)))
        start = round(start*(1+intrestRate), 4)

print("""
Functions in the file:
fraction('str')
equationOfLineToSlopeInterceptForm(i = True, autoReduce = True)
EQOLBTP(point1, point2) equation of line between two points.
imperialToMetric(ft, in) convert to cm.
checkForParallelOrPerpendicular(slope1, slope2)
slopeInterceptFormGetSlope(i = True, autoReduce = True)
perpendicularLinePassingThroughPoint(slope, (pointx, pointy))
parallelLinePassingThroughPoint(slope, pointx, pointy)
""")

######Here are the test calls for the functions.
##fraction(i = '1/2+1/4')
##fraction(i = '1/2--1/4')
##fraction(i = '1/2*1/4')
##fraction(i = '1/2//1/4')
##EQOLBTP((-1, -5), (-5, 1))
##s1 = equationOfLineToSlopeInterceptForm(i = '10x+4y=-4', autoReduce = True)
##s2 = slopeInterceptFormGetSlope(i = '2y=5x+7')
##checkForParallelOrPerpendicular(s1, s2)
perpendicularLinePassingThroughPoint('4/3', -6, 4)
print('--------------------------------------')
parallelLinePassingThroughPoint('-3/4', -6, 4)
