##Nathan Hinon
##This is the main program for algebra 2

print("Setting up...")
import Factor
import takeInput

def trinomial():
    #x**2+(a+b)x+ab
    i = takeInput.rawInput()
    seperate = i.split('+')
    print(seperate)
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

