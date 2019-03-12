##Nathan Hinton
##
##This program calcluates the: area, uses pathag to find a missing side, uses

##To do:
#Convert the program into a class.

class Triangle:
    def __init__(self):
        import math as m
        self.m = m

    def area(self):
        self.base = input("base  ")
        self.height = input("height  ")
        print(int(self.base)*int(self.height)/2)

    def pathag(self):
        self.side1 = input("side1  ")
        self.side2 = input("side2  ")
        print(self.m.sqrt(int(self.side1)**2+int(self.side2)**2))
        print()
        print(int(self.side1)**2 + int(self.side2)**2)
    def permiter(self):
        self.a = input("Side 1  ")
        self.b = input("Side 2  ")
        self.c = input("Side 3  ")
        print(int(self.a)+int(self.b)+int(self.c))

        ##start TRI help
    def help(self):
        print("Help for Triangle file")
        print("""
    This is the help function for the Triangle.py file.  Some things may be
    outdated as you use different versions of the main program or just the
    plain program.    """)
        print()
        print("""Here is a list of Triangle commands.  they are defined in the
              Triangle file and if they are used with a wrapper they may be
              different.""")
        print("""
    self.help()-------Show TRI help.
    self.area()-----Triangle area.
    self.pathag()---Triangle calcluate side for right triangle using pathag.
    self.permiter()-----Triangle calcluate the permiter of a triangle
        """)
    ##end TRI help

def run():
    t = Triangle()
    print("1:area")
    print("2:pathag")
    print("3:permiter")
    i = input()
    if i == '1':
        t.area()
    elif i == '2':
        t.pathag()
    elif i == '3':
        t.premiter()
    else:
        print("Invalid input")
print("Done loading Triangle programm")
print("!!!THIS PROGRAM HAS BEEN CONVERTED INTO A CLASS! IT MAY NOT FUNCTION IN OLDER PROGRAMS!!!")
