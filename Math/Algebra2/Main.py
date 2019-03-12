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

def calcTri(mult, a, b):#V2
    #x+y = a
    #x*y = b
    #Get the sets of factors.
    sets = []
    nums = Factor.factor(b)
    for x in range(int(len(nums)/2)):
        sets.append([nums[x*2], nums[x*2+1]])
    #there should be 4 combonations for wach set of numbers.
    for s in sets:
        if s[0]+mult*s[1] == a:#If they are both positive:
            return s[0], s[1]
        elif -s[0]+mult*s[1] == a:#If the first is neg:
            return -s[0], s[1]
        elif s[0]+-mult*s[1] == a:#If the second is neg:
            return s[0], -s[1]
        elif -s[0]+-mult*s[1] == a:#If both are is neg:
            return -s[0], -s[1]
    
def extractNum(string):#V1
    #This will extract numbers from the begining of strings.
    final = 0
    temp = []
    neg = 1
    for s in range(len(string)):
        try:
            if string[s] == '-':
                neg = -1
            else:
                i = int(string[s])
                temp.append(i)
        except ValueError:
            break
    #print(temp)
    for x in range(len(temp)):
        #print(temp[x]*10**(len(temp)-x-1))
        final += temp[x]*10**(len(temp)-x-1)
    return final*neg
                

def trinomial():#V1
    #x**2+(a+b)x+ab
    #Forms:
    #x**2+7x+12
    #(x+a)(x+b)
    i = takeInput.rawInput()
    seperate = tsplit(i, ('-', '+'))
    print(seperate)
    #print(seperate[1])
    mult = extractNum(seperate[0])
    poly1 = extractNum(seperate[1])
    poly2 = extractNum(seperate[2])
    a, b = calcTri(mult, poly1, poly2)
    print(a, b)
    print('(%ix+%i)(x+%i)'%(mult, a, b))
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
