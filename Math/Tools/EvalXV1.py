##Nathan Hinton
##This is a program that will return an equation with x for evaluation.

def i():
    print("Enter the equation:")
    return str(input())
def FindTheX(i):
    running = True
    state = 'init'
    length = len(i)
    xpos = []
    while running == True:
        if state == 'init':
            pos = 0
            state = 'isX'
        elif state == 'isX':
            print(pos)
            if pos == length:
                running = False
            else:
                if i[pos] == 'x' or i[pos] == 'X':
                    xpos.append(pos)
                pos += 1
    return i, xpos
def testV2():#Goal: make it so that you can move the x around
    pass
#####################################################
def testV1(rangeMin = -1, rangeMax = 2):
    print("TEST V1")
    dat = i()
    data, xpos = FindTheX(dat)
    print(data)
    print(xpos)
    for x in range(rangeMin, rangeMax):
        equ = str(data[0:xpos[0]]+str(x)+data[xpos[0]+1:len(data)])
        #print(type(equ))
        #print(equ)
        print(equ+':'+str(eval(equ)))


##Here is the program being tested
testV1()
