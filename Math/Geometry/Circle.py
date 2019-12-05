import math as m
def area():
    radius = input("radius  ")
    print(m.pi*int(radius)**2)
def permiter():
    radius = input("radius  ")
    print(int(radius)*m.pi*2)

def help():
    print("Help for CIR set")
    print("""
The way that this was designed was to make it so you enter CIR and that stands
for Circle, then you enter the first leters of what you want to do in caps
and after the last capital leter you put the next leter of the function an
lowercace.  Example: for the area of a circle you put CIR with Ar for area
right after to make CIRAr.
    """)
    print()
    print("Here is a list of Circle commands")
    print("""
CIR-------Show CIR help.
CIRAr-----Circle area.
CIRPe-----Circle calcluate the permiter of a triangle
    """)
##end CIR help

def run():
    print("1:area")
    print("2:permiter")
    i = input()
    if i == '1':
        area()
    elif i == '2':
        permiter()
    else:
        print("Invalid Input")

print("Done loading Circle programms")
