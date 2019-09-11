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
            if '//' in i:
                state = 'divide'
            elif '*' in i:
                state = 'mult'
            elif '-' in i:
                state = 'subtract'
            elif '+' in i:
                state = 'add'
            else:
                print("fraction state machine error. No modifier found. Aborting.")
                state = 'end'
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
            frac1, frac2 = i.split('-')
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
            for x in range(2, finalBottom):
                if finalTop%x == 0:
#                    print(x)
                    finalTop = finalTop/2
                    finalBottom = finalBottom/2
                    break
            state = 'end'
#        sleep(1)
    print('%s/%s'%(int(finalTop), int(finalBottom)))
    return (finalTop, finalBottom)
        

print("""
Functions in the file:
fraction('str')
""")

####Here are the test call for the functions.
fraction(i = '1/2+1/4')
fraction(i = '1/2-1/4')
fraction(i = '1/2*1/4')
fraction(i = '1/2//1/4')

