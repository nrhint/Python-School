#Nathan Hinton
#This is another way of approaching the math functions.
#Here you will need to call all of the functions them selves.
#I will make a help function that will list all of the functions.

print("Starting...")

import Circle
import Cuboid
import Cylinder
import Fractions
import Prism ##May be having troubles.
import Sphere
import Square
import Triangle

print("Done loading the programs.  Thanks!")

print("Creating user interface...")
run = True
while run == True:
    print("0:exit")
    print("1:circle")
    print("2:cuboid")
    print("3:cylinder")
    print("4:fractions")
    print("5:prism")
    print("6:sphere")
    print("7:square")
    print("8:triangle")
    i = input()
    if i == '0':
        run = False
        print("Thank you!")
    elif i == '1':
        Circle.run()
    elif i == '2':
        Cuboid.run()
    elif i == '3':
        Cylinder.run()
    elif i == '4':
        Fractions.run()
    elif i == '5':
        Prism.run()
    elif i == '6':
        Sphere.run()
    elif i == '7':
        Square.run()
    elif i == '8':
        Triangle.run()
    else:
        print("Invalid input...")
    
