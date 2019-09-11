##Nathah hinton
##this will contain all of the helper functons that I have built.

from time import sleep
from random import randint as rint

def fraction(i = True):
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
            for x in range(2, abs(finalBottom)+1):
                if finalTop%x == 0 and finalBottom%x == 0:
#                    print(x)
                    finalTop = finalTop/2
                    finalBottom = finalBottom/2
                    break
            state = 'end'
#        sleep(1)
    print('%s/%s'%(int(finalTop), int(finalBottom)))
    return (int(finalTop), int(finalBottom))

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

print("""
Functions in the file:
fraction('str')
equation of line between two points. EQOLBTP(point1, point2)
""")

####Here are the test calls for the functions.
#fraction(i = '1/2+1/4')
#fraction(i = '1/2-1/4')
#fraction(i = '1/2*1/4')
#fraction(i = '1/2//1/4')
#EQOLBTP((-1, -5), (-5, 1))

