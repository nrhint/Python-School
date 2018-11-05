##Nathan Hinton
#
#TODO:
#FINISH ADDING THE AMU TO THE ELELIST

##In progress/copied works:
"""
dat = open(file, 'r')
dat = dat.read()
dat.replace('\n', ' | ')#Remove the newlines and add the pipes to seperate elements.
lst1 = dat.split(' ')

"""


#import stuff
print("Importing")
import pickle#for loading the file

def __init__():
    #Load the file as eleList
    print("Loading File")
    pklFile = 'elementlist.pkl'
    dat = pickle.load(open(pklFile, 'rb'))#open('/NathanShare/School/Science2018-2019/elementlist.pkl', 'rb'))
    #dat = dat.read()
    dat = dat.replace('\n', '|')#Remove the newlines and add the pipes to seperate elements.
    eleList = dat.split('|')
    ###########################################
    print("Defining stuff")
    valance = [2, 10, 18, 36, 54, 86, 118]
    MOLE = 6.02*10**27
    return pklFile, eleList, valance, MOLE

#Calc Atom stuff

def updatePkl(fname, pklFile):
    newDatFile = open(str(fname), 'r')
    newDat = newDatFile.read()
    newDatFile.close()
    print("Loaded data to newDat.  here is data: %s" %newDat)
    print("Backing up pkl file...")
    origPkl = open(pklFile, 'rb')
    bupPkl = open(pklFile+'.bup', 'wb')
    bupPkl.write(origPkl.read())
    bupPkl.close()
    origPkl.close()
    print("pkl backed up. rewriting data to pkl...")
    origPkl = open(pklFile, 'wb')
    pickle.dump(newDat, origPkl)
    origPkl.close()
    print("Data written!")
    print()
    print("Program restart required for changes to make affect.")
    #print("<<<NOT FINISHED>>>")

def PL(item):
    print('PL (ProcessList) was ran.')
    lst = []
    #Process string:
    if type(item) == str:
        lst = item.split(' ')
    else:
        print()
        print("                !!!WARNING!!!")
        print("Unknown or unrecognized data type. returning empty list")
    return lst

def CalcAtom():
    print("Type 0 or 1")
    i = int(input())
    try:
        if i == 0: #When you have the parts not the name
            z = int(input("Protons: "))# (Number of Protons)
            e = int(input("Electrons: "))# (Number of Electrons)
            n = int(input("Neutrons (None if unknown): "))# (Number of Neutrons)

            if n == 'None':
                a = "Not able to find!"
            else:
                a = z+n
            charge = z-e

            #Atom number = Z
            #Atomic mass = A

            print('Element is: \n'+str(eleList[z-1]))
            print('Protons: '+str(z))
            print('electrons: '+str(e))
            print('Neutrons: '+str(n))
            print('Atomic weight: '+str(a))
            print('Charge: '+str(charge))
        elif i == 1: #Other stff
            z = int(input("Protons: "))# (Number of Protons)
            #e = int(input("Electrons: "))# (Number of Electrons)
            #n = int(input("Neutrons: "))# (Number of Neutrons)
            charge = int(input("Charge: "))
            a = int(input("Mass: "))

            #a = z+n
            n = a-z
            #charge = z-e
            e = z-charge

            #Atom number = Z
            #Atomic mass = A

            print('Element is: \n'+str(eleList[z-1]))
            print('Protons: '+str(z))
            print('electrons: '+str(e))
            print('Neutrons: '+str(n))
            print('Atomic weight: '+str(a))
            print('Charge: '+str(charge))
        else:
            print("Error")
    except IndexError:
        print("Index error! This could be from missing data in the pkl file. Try running the update function to make sure that the data matches.  This also could be caused by a bug in the progtam.  If you look in the elementlist.txt file and make sure that the data you are requesting is there and then update the pkl file and the error persists then there is an error in the program.")

def SearchAtom(char):
    print("Please put all of the chars in LOWERCASE")
    if len(char) > 2:
        for x in range(len(eleList)):
            ele = eleList[x].lower()
            if str(char) == ele[2].lower():
                print(ele)
    else:
        for x in range(len(eleList)):
            ele = eleList[x]
            if str(char) == ele[1].lower():
                print(ele)
            #print(x)

def Seperate(lst, item):
    x = eleList[lst]
    try:
        return x[item]
    except IndexError:
        print("Item was to large! You made an index error.  Please make item smaller and try again!")
        
pklFile, eleList, valance, MOLE = __init__()
