##Nathan Hinon
##This is the main program for algebra 2

print("Setting up...")
import Factor
import takeInput

#tsplit came from:
#http://code.activestate.com/recipes/577616-split-strings-w-multiple-separators/
def tsplit(string, delimiters):
    """Behaves str.split but supports multiple delimiters."""
    delimiters = tuple(delimiters)
    stack = [string,]
    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i+j, _substring)
    return stack

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
    a, b = calcTri(poly1, poly2)
    print(a, b)
    print(neg)
    if neg == True:
        print('(x-%i)(x+%i)'%(a, b))
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

