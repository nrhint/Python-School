##Nathan Hinton
##This program will factor a number.
##I plan to use it for factoring radicals

from math import sqrt as sq

def factor(num):
    if num > 9999999999999:
        print("Number To large and may take a while to do.")
        return 0
    factors = []
    lastFact = 1
    for x in range(1, int(num/2)+1):
        if num%x == 0:
            if lastFact == num/x:
                break
            elif x == num/x:
                factors.append(x)
                break
            #print(x, num/x)
            factors.append(x)
            factors.append(int(num/x))
            lastFact = x
    return factors

def findSquares(num):
    facts = factor(num)
    facts.sort()
    print(facts)
    end = len(facts)-1
    m = sq(facts[end])+1
    #3print(m)
    for x in range(0, int(m)):
        if x == 1:
            pass
        elif x**2 in facts:
            print(x)
    
