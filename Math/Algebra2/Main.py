##Nathan Hinon
##This is the main program for algebra 2

print("Setting up...")
import Factor
import takeInput

def calcTri(a, b):
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

def trinomial():
    #x**2+(a+b)x+ab
    #Forms:
    #x**2+7x+12
    #(x+a)(x+b)
    i = takeInput.rawInput()
    seperate = i.split('+')
    print(seperate)
    #print(seperate[1])
    for x in range(len(seperate[1])):
        if x == '-':
            poly1 = int(seperate[1][0:1])
        else:
            poly1 = int(seperate[1])
    for x in range(len(seperate[2])):
        if x == '-':
            poly2 = int(seperate[2][0:1])
        else:
            poly2 = int(seperate[2])
    a, b = calcTri(poly1, poly2)
    print(a, b)
    print('(x+%i)(x+%i)'%(a, b))
    return seperate

#Main loop:
mainLoop = True
while mainLoop == True:
    print()
    print("0:Exit")
    print("1:Factor Radical")
    print("2:Simplify Trinomial")
    print("3:Eval Quadratic equation")
    ans = str(input())
    if ans == '0':#Exit
        print("Thank you!")
        mainLoop = False
    elif ans == '1':#Factor radical
        print("Number in radical:")
        Factor.print_reduced_sqrt(takeInput.rawInput())
    elif ans == '2':#Eval Trinomial
        print("In Progress...")
        print("Enter Trinomaial:")
        trinomial()
    elif ans == '3':#Eval Quadratic
        print("In Progress.")
    else:
        print("Invalid input: %s" %ans)

