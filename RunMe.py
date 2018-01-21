##To do list
## finish defining the TSA, permiter, and volume if a cuboid
##finish adding the commands for Cuboid
##start/finish adding the commands for Fractions
##

##setup lists

COMMANDS = [
    'exit', 'h', 'TRI', 'TRIAr', 'TRICFTr', 'TRICSRt', 'TRIPe', 'CIRAr',
    'CIRPe', 'CIR', 'SQU', 'SQUAr', 'SQUPe'
            , 'nope']
try:
    commands = COMMANDS.copy()
    commands.pop()
except AttributeError:
    print("!!!COULD NOT CREATE COPY OF COMMANDS!!!")
    commands = COMMANDS
    commands.pop()

####import required files
##import Triangle as TRI
##import Square as SQU
##import Circle as CIR
##import Cuboid as CUB
##import Fractions as FRA
##import Cylinder as CYL


def runProg():
    ##import required files
    import Triangle as TRI
    import Square as SQU
    import Circle as CIR
    import Cuboid as CUB
    import Fractions as FRA
    import Cylinder as CYL
    import Sphere as SPH
    import math as M
    print("finished importing math as M")
    #start program
    print("Starting program")
    print("Type exit to end program")
    print("Enter h to access the help function")
    for x in range(0, 2):
        print()

    ##setup vars

    end = False
    check = True


    ##Main loop
    while end == False:
        check = True
        print()
        ##take user input as to what to do
        user = input("What do you want me to do?  ")
        ##check to make sure that the command is a valid command
        for x in range(len(COMMANDS)):
            if COMMANDS[x] == 'nope' and check == True:
                print("Command not in database")
                print()
            elif user == COMMANDS[x]:
                check = False
        ##start to run the command that has ben verified

        ##exit function
        if user == 'exit':
            end = True
            print("type: runProg() to run the programm again")
        ##help function
        elif user == 'h':
            h()
        ##help for TRI function
        elif user == 'TRI':
            TRI.help()
        ##find the area of a triangle
        elif user == 'TRIAr':
            TRI.area()
        ##find out if a set of therr numbers is a pathag tripple
        elif user == 'pathag':
            TRI.pathag()
        ##calcluate the remaining side of a right triangle using pathag
        elif user == 'TRICSRt':
            TRI.calcSideRight()
        ##calcluate the perimeter of a triangle
        elif user == 'TRIPe':
            TRI.permiter()
        ##calcluate the area of a circle
        elif user == 'CIRAr':
            CIR.area()
        ##calcluate the permiter of a circle
        elif user == 'CIRPe':
            CIR.permiter()
        ##circle help
        elif user == 'CIR':
            CIR.help()
        ##Square help
        elif user == 'SQU':
            SQU.help()
        ##find the area of a square
        elif user == 'SQUAr':
            SQU.area()
        ##find the permiter
        elif user == 'SQUPe':
            SQU.permiter()
        ##do the fraction program
        elif user == 'FRA':
            FRA.run()
        ##fraction help
        elif user == 'FRA':
            FRA.help()
        ##Cuboid help
        elif user == 'CUB':
            CUB.help()
        ##find the area of a cuboid
        elif user == 'CUBAr':
            CUB.area()
        ##find the volume of a cubiod
        elif user == 'CUBVo':
            CUB.volume()
        ##find the permiter of a cuboid
        elif user == 'CUBPe':
            CUB.permiter()
        #Find the volume of a sphere
        elif user == 'SPHVo':
            SPH.volume()
        #Find the surface ares ofa sphere
        elif user == 'SPHAr':
            SPH.area()
        #Find the surface area of a cylinder
        elif user == 'CYLAr':
            CYL.area()
        #Find the volume of a cylinder
        elif user == 'CYLVo':
            CYL.volume()

##def runProg2():
####    ##import required files
####    import Triangle as TRI
####    import Square as SQU
####    import Circle as CIR
####    import Cuboid as CUB
####    import Fractions as FRA
####    import Cylinder as CYL
##    #start program
##    print("Starting program")
##    print("Type exit to end program")
##    print("Enter h to access the help function")
##    for x in range(0, 2):
##        print()
##
##    ##setup vars
##
##    end = False
##    check = True
##
##
##    ##Main loop
##    while end == False:
##        check = True
##        print()
##        ##take user input as to what to do
##        user = input("What do you want me to do?  ")
##        ##check to make sure that the command is a valid command
##        for x in range(len(COMMANDS)):
##            if COMMANDS[x] == 'nope' and check == True:
##                print("Command not in database")
##                print()
##            elif user == COMMANDS[x]:
##                check = False
##        ##start to run the command that has ben verified


def h():
    print("WARNING: Command in Progress")
    print("here is a list of commands that can be executed:")
    print(commands)
    print()
    print("here is a structure of the command set:")
    print("""Line numbera are approximate.
Local commands:
command|line number|
exit   |41         |
help   |45         |
____________________
External commands:
command |full name            |local line number |file name |file line number|
TRI     |TRI.help             |53                |Trinagle  |35              |
TRIAr   |TRI.area             |56                |Triangle  |1               |
TRICFTr |TRI.checkForTripple  |59                |Triangle  |5               |
pathag  |TRI.pathag           |62                |Triangle  |17              |
TRIPe   |TRI.permiter         |65                |Triangle  |28              |
CIRAr   |CIR.area             |68                |Circle    |2               |
CIRPe   |CIR.permiter         |71                |Circle    |5               |
CIR     |CIR.help             |74                |Circle    |9               |
SQU     |SQU.help             |77                |Square    |12              |
SQUAr   |CIR.area             |80                |Square    |1               |
CIRPe   |CIR.permiter         |83                |Square    |5               |
FRAr    |FRA.run              |86                |Fractions |1               |
CUB     |FRA.help             |89                |Cuboid    |16              |
CUBAr   |CUB.totalSurfaceArea |72                |Cuboid    |1               |
CUBVo   |CUB.volume           |95                |Cuboid    |6               |
CUBPe   |CUB.permiter         |98                |Cuboid    |11              |
________________________________________________________________________
External files:
Geometry.py
Fractions.py
Pathag.py

            """)
    print()
    print("Type the first three leters of a command to see more speciffic help for that command.")


runProg()
