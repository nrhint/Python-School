##Nathan Hinton
##
##This program calcluates the: area, uses pathag to find a missing side, uses
##pathag to vhevk for a pathag tripple.

##To do:

import math as m

def area():
    base = input("base  ")
    height = input("height  ")
    print(int(base)*int(height)/2)
def checkForTripple():
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    if m.sqrt(int(a)**2+int(b)**2) == int(c):
        print("a^2+b^2=c^2")
    elif m.sqrt(int(b)**2+int(c)**2) == int(a):
        print("b^2+c^2=a^2")
    elif m.sqrt(int(c)**2+int(a)**2) == int(b):
        print("c^2+a^2=b^2")
    else:
        print("False")
def pathag():
    side1 = input("side1  ")
    side2 = input("side2  ")
    print(m.sqrt(int(side1)**2+int(side2)**2))
    print()
    print(int(side1)**2 + int(side2)**2)
def permiter():
    a = input("Side 1  ")
    b = input("Side 2  ")
    c = input("Side 3  ")
    print(int(a)+int(b)+int(c))

    ##start TRI help
def help():
    print("Help for TRI set")
    print("""
The way that this was designed was to make it so you enter TRI and that stands
for Triangle, then you enter the first leters of what you want to do in caps
and after the last capital leter you put the next leter of the function an
lowercace.  Example: for the area of a triangle you put TRI with Ar for area
right after to make TRIAr.
    """)
    print()
    print("Here is a list of Triangle commands")
    print("""
TRI-------Show TRI help.
TRIAr-----Triangle area.
TRICFTr---Triangle check for Tripple.
pathag---Triangle calcluate side for right triangle using pathag.
TRIPe-----Triangle calcluate the permiter of a triangle
    """)
##end TRI help


print("Done loading Triangle programms")
