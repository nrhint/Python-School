##Nathan Hinton.
##This program will take input and then return the output one characater at a time as a str or an int. It is ment to be used for state machines.

#When program done comment all printing
print("Initalizing takeInput.py...")
print("Does not handle lists. only strings")

def takeUserInput():
    #Take input
    print("Input:")
    i = input()
    dat = []

    #Process input
    for char in i:
        try:
            dat.append(int(char))
        except ValueError:
            dat.append(str(char))
    #return the list of values as ints and chars.
    return dat

def takeInput(i):
    #Take input
    dat = []

    #Process input
    for char in i:
        try:
            dat.append(int(char))
        except ValueError:
            dat.append(str(char))
    #return the list of values as ints and chars.
    return dat

def rawInput():
    return input()
