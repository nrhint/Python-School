###Nathan Hinton
#This file contains old code from programs

#This is V1 of calc Tri. only handles positive tris.
#State: Broken?
def calcTri(a, b):#V1
    x1 = 0
    x2 = 0
    while x1 < a:
        x1 +=1
        x2 = 0
        #print('x1:%s'%+x1)
        while x2 < a:
            x2 +=1
            #print('x2:%s'%+x2)
            if x1+x2 == a and x1*x2 == b:
                return(x1, x2)

#State working with calcTriV1
def trinomial():#V1
    #x**2+(a+b)x+ab
    #Forms:
    #x**2+7x+12
    #(x+a)(x+b)
    i = takeInput.rawInput()
    seperate = tsplit(i, ('-', '+'))
    print(seperate)
    #print(seperate[1])
    x = seperate[1][0]
    neg = False
    if x == '-':
        neg = True
        poly1 = int(seperate[1][1])
    else:
        poly1 = int(seperate[1][0])
    x = seperate[2][0]
    if x == '-':
        neg = True
        poly2 = int(seperate[2][1])
    else:
        poly2 = int(seperate[2])
    a, b = calcTri(mult, poly1, poly2)
    print(a, b)
    print(neg)
    if neg == True:
        print('(x-%i)(x+%i)'%(a, b))
    print('(x+%i)(x+%i)'%(a, b))
    return seperate


