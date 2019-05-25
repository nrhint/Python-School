##Nathan Hinton
##This is a program that will return an equation with x for evaluation.

def i():
    print("Enter the equation:")
    return str(input())
def removeSpaces(i):#Remove spaces from input so that long equations take less time.
    i2 = i.split()
    i3 = ''
    for x in i2:
        i3 += x
    return i3
def FindTheX(i):#This will find x.
    i = removeSpaces(i)
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
def moveX(i):
    running = True
    state = 'init'
    output = i
    #Find which side x is on:
    left = i.split('=')[0]
    right = i.split('=')[1]
    if 'x' in left:
        side = 'left'
    else:
        side = 'right'
    while running == True:
        if state == 'init':
            print("Starting move x...")
            state = 'multDiv'
        elif state == 'test':
            if '*' in output or '/' in output:
                state = 'multDiv'
            elif '+' in output or '-' in output:
                state = 'addSub'
            else:
                state = 'end'
        elif state == 'multDiv':
            temp = i
            splt = temp.split('x')#Find a place where x is.
            xexpr = splt[0]
            #Check for multuplication:
            if '*' in xexpr:
                print('mult')
                l = len(xexpr)
                loop = 1
                end = 0
                for x in range(-l+2, 1):
                    num = ''
                    item = xexpr[-x]
                    #print(item)
                    if item == '*':
                        end = -x
                    elif item == '/':
                        end = -x
                    elif item == '+':
                        end = -x
                    elif item == '-':
                        end = -x
                    else:
                        num +=str(int(item)*10**(loop-1))
                    loop += 1
                if side == 'left':
                    tmpExpr = right+'/'+str(num)
                    output = str(i[0:end])+'x='+tmpExpr
                    print('left')
                else:
                    tmpExpr = left+'/'+str(num)
            i = i.replace('*', '&', 1)#remove the * from the equation
            state = 'test'
        elif state == 'addSub':
            pass
        elif state == 'end':
            print("Finished")
            print(output)
            return output
def testV2():#Goal: make it so that you can move the x around
    print("Test V2")
    rawEquation = i()
    equation, xPos = FindTheX(rawEquation)
    print(equation, xPos)
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
#testV2()
i = '5*x=32'
moveX(i)
