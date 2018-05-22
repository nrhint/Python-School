##This is the nmain file for the python math.
##Nathen Hinton

from math import *

def prime(number):
    print("Working...")
    sq = sqrt(number)
    div = 1
    result = True
    while div < sq+1 and result == True:
        div +=1
        if number % div == 0:
            result = False
    return result

