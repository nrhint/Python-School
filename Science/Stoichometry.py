##Nathan Hinton
#
#TODO:
#Moving the extra nonBasic functions to the bottom and remaking them with newer functions and processing.

#import stuff
print("Importing")
import pickle#for loading the file

#Setup state machine error:
class StateMachineError(Exception):
    pass

###COMMENT FORMAT###

#'Version', is fixing needed

#Main class
class Stoichometry:
#########################Stuff to use for later input and data#################
    def __init__(self, mode):#Version 1 unknown
        #Load the file as eleList
        print("Loading Element File")
        if mode == 'direct':
            import sys
            self.pklFile = sys.path[0]+'/Science/elementlist.pkl'
        else:
            self.pklFile = 'elementlist.pkl'
        self.dat = pickle.load(open(self.pklFile, 'rb'))#open('/NathanShare/School/Science2018-2019/elementlist.pkl', 'rb'))
        #dat = dat.read()
        self.dat = self.dat.replace('\n', '|')#Remove the newlines and add the pipes to seperate elements.
        self.eleList = self.dat.split('|')
        ###########################################
        print("Defining stuff")
        self.valance = [2, 10, 18, 36, 54, 86, 118]
        self.MOLE = 6.02*10**27
        self.item = None
        #return pklFile, eleList, valance, MOLE

    #Calc Atom stuff

    def updatePkl(self, fname, pklFile):#Version 2 unknown:
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
        self.__init__()
        #print("Program restart required for changes to make affect.")
        #print("<<<NOT FINISHED>>>")

    def PD(self, item):#Version 1 unknown
        #print('PD (ProcessData) was ran.')
        self.lst = []
        #Process string:
        if type(item) == str:
            self.lst = item.split(' ')
        elif type(item) == list:
            for x in range(len(item)):
                try:
                    self.lst.append(float(item[x]))
                except ValueError:
                    print("ValueError processed")
                    self.lst.append(item[x])
        else:
            print()
            print("                !!!WARNING!!!")
            print("Unknown or unrecognized data type. returning empty list")
        return self.lst
#REMOVED CalcAtom and main
    def findAtom(self, char):#Version 1 unknown
        for x in range(len(self.eleList)):
            #print(eleList[x]) #Noise reduction
            ele = self.PD(self.eleList[x])
            #print()
            #print(ele)
            try:
                if ele[1].lower() == str(char.lower()):
                    print(ele)
                    return(ele)
                if ele == '':
                    print("''")
            except IndexError:
                print("IndexError processed.")
                print("Elemment not in the list or the abbr was typed wrong")
                self.findAtom(input("Try again, element:  "))

    def amu(self, eleDat):#Version 1 unknown
        self.result = 0
        #print(len(eleDat))
        for w in range(0, len(eleDat)):
            #print(w)
            #print(eleDat[w][3])
            self.result += float(eleDat[w][3])
        return self.result
#REMOVED stoi and stoi2 and limitReagent and SearchAtom
    def findInList(self, lst, item):#Version 1 unknown
        x = self.eleList[lst]
        try:
            return x[item]
        except IndexError:
            print("INDEX ERROR, something went wrong with you input")

    def PC(self):#Version 1 Needs to have a ratio(nuber in front)
        #Process compound This is the first state machine I have Made!
        self.i = str(input("Compound: "))

        ##if i[x].isupper():
        ##    state = 'upper'
        ##elif i[x].islower():
        ##    state = 'lower'
        ##elif i[x].isdigit():
        ##    state = 'digit'
        ##else:
        ##    raise StateMachineError


        state = 'init'
        self.element = ''
        self.mult = 1
        self.number = 1
        self.finalData = []
        def commit():
            for l in range(int(self.number)):
                self.finalData.append(self.element)
            self.number = 1
            self.element = ''

        for x in self.i:
            print(state)
            print(self.number)
            if state == 'init':
                if x.isupper():
                    self.element += x
                    state = 'upper'
                elif x.isdigit():
                    self.mult += int(x)-1
                    state = 'init'
                else:
                    raise StateMachineError("@init expected upper char", state)
            elif state == 'upper':#Done
                if x.isupper():
                    commit()
                    self.element += x
                elif x.islower():
                    self.element += x
                    state = 'lower'
                elif x.isdigit():
                    self.number += int(x)-1
                    state = 'digit'
                else:
                    raise StateMachineError("@ upper unexpected char", state)
            elif state == 'lower':
                if x.isupper():
                    commit()
                    self.element += x
                    state = 'upper'
                elif x.isdigit():
                    self.number += int(x)-1
                    state = 'digit'
                else:
                    raise StateMachineError("@ lower expected upper or digit", state)
            elif state == 'digit':
                if x.isupper():
                    commit()
                    self.element += x
                    state = 'upper'
                elif x.isdigit():
                    self.number = self.number*10
                    self.number += int(x)
                else:
                    raise StateMachineError("@ Digit expected upper", state)
            else:
                raise StateMachineError("@StateMachine expected something, I dont know what", state)
        commit()
        return self.finalData
    
    def inp(self):#Version 1 unknown
        #Input for the program.
        self.PC()
        self.inpDat = []
        print(self.finalData)
        for x in range(len(self.finalData)):
            item = self.finalData[x]
            #print(item)
            elem = self.findAtom(item)
            self.inpDat.append(elem)
            #print(elem)
        return self.inpDat#What type of data is returned?

    def lmtReagent(self):
        #Setup vars/reset vars:
        self.weight1 = 0
        self.weight2 = 0
        print("The first compound:  ")
        self.dat1 = self.inp()
        self.mult1 = self.mult
        print("The second compound:  ")
        self.dat2 = self.inp()
        self.mult2 = self.mult
        print("DATA:")
        print(self.dat1)
        print(self.dat2)
        print()
        print()
        #ADD AMU V2:
        self.weight1 = round(float(input("Mass of first compound:  "))/self.amu(self.dat1), 8)
        self.weight2 = round(float(input("Mass of second compound:  "))/self.amu(self.dat2), 8)
        #Final code for comparisan and final output.
        if self.mult1<self.mult2:
            self.multLarge = self.mult2
        else:
            self.multLarge = self.mult1
        print(self.multLarge)
        print(self.weight1, self.weight2)
        print(self.weight1/self.mult1, self.weight2/self.mult2)
        if self.weight1/self.mult1<self.weight2/self.mult2:
            print("1 is less")
            self.weight = self.weight1
            self.mul = self.mult1
        elif self.weight1/self.mult1>self.weight2/self.mult2:
            print("2 is less")
            self.weight = self.weight2
            self.mul = self.mult2
        else:
            print("!!!BALLANCED WEIGHT OR ERROR!!!.")
            self.weight = self.weight1
            self.mul = 'Error'
        print("What is the end result")
        self.dat3 = self.inp()
        self.mult3 = self.mult
        self.weight3 = self.amu(self.dat3)
        self.answer = self.weight/(self.mul/self.mult3)#HERE IS THE PROBLEM
        print()
        print("Moles: ", self.weight1, self.weight2, self.weight3)
        print("AMUs: ", self.amu(self.dat1), self.amu(self.dat2), self.amu(self.dat3))
        print("Answers:")
        print("Moles: %s"%self.answer)
        print("Grams: %s"%(self.answer*self.weight3))
    def GtoM(self):
        self.dat = self.inp()
        self.weight = round(float(input("Mass of compound:  "))/self.amu(self.dat), 8)
        print("Moles: "+self.weight)
    def MtoG(self):
        self.dat = self.inp()
        self.weight = round(float(input("Moles of compound:  "))*self.amu(self.dat), 8)
        print("Grams: "+self.weight)
    def convert(self):
        print("1: Grams to Moles")
        print("2: Moles to Grams")
        self.i2 = input()
        if self.i2 == '1':
            self.GtoM()
        elif self.i2 == '2':
            self.MtoG()
        else:
            print("ERROR!")
    def stoi(self):
        self.GtoM()
        
#        self.dat = self.inp()
#        self.weight = self.amu(self.dat)
#        print(self.weight)
#        print("Processing data...")
    def Mwp(self):#Molecular weight percentages:
        self.dat = self.inp()
        #Count the stuff in the dat:
        self.mp = {}
##        #This adds each molicule to the list to a map
##        for x in range(len(self.dat)):
##            if self.dat[x][1] not in self.mp:
##                self.mp.update({self.dat[x][1]:1})
##            elif self.dat[x][1] in self.mp.keys():
##                self.num = self.mp[self.dat[x][1]]
##                print(self.num)
##                self.mp.update({self.dat[x][1]:(self.num+1)})
##        #Take the mapped values and then
        self.total = 0
        for x in range(len(self.dat)):
            if self.dat[x][1] not in self.mp:
                self.total += float(self.dat[x][3])
                self.mp.update({self.dat[x][1]:self.dat[x][3]})
            elif self.dat[x][1] in self.mp.keys():
                self.total += float(self.dat[x][3])
                self.num = self.mp[self.dat[x][1]]
                print(self.num)
                self.mp.update({self.dat[x][1]:(round(float(self.num)+float(self.dat[x][3]), 4))})
        self.total = round(self.total, 4)
        #calculate the percentages
        print(self.mp)
        print(self.total)
        print()
        for x in self.mp:
            print(x+' : %'+str((self.mp[x]/self.total)*100))

    def MassCompToEmp(self):
        run = True
        self.pct = []
        self.atm = []
        #Take the input from user
        while run == True:
            self.atm.append(input("Atom: "))
            self.pct.append(int(input("Atom Percent: ")))
            if input("Finished? Y or nothing: ") == 'Y':
                run = False
        #Process input and calculate moles:
        print(self.atm)
        print(self.pct)
        for x in range(len(self.atm)):
            dat = self.findAtom(self.atm[x])
            print(dat[3])
            print(self.pct[x])
    def calcValance(self):
        self.dat = self.inp()
        self.num = int(self.dat[0][0])
        run = True
        for x in self.valance:
            if self.num>x:
                print(self.num-x)
            else:
                self.v = x
                break

    def main(self):
        print("1: Limiting reagent")
        print("2: Find element and data")
        print("3: Convert moles and grams")
        print("4: Molecular weight percentages")
        print("5: Mass composition to empirical")
        print("6: Calculate valance electrons")
        self.i = input()
        if self.i == '1':
            self.lmtReagent()
        elif self.i == '2':
            print("Element abbr: ")
            self.findAtom(input())
        elif self.i == '3':
            self.convert()
        elif self.i == '4':
            self.Mwp()
        elif self.i == '5':
            self.MassCompToEmp()
        elif self.i == '6':
            self.calcValance()
        else:
            print("Input error or method not defined!")
        self.main()
################################################################################
print("Autorun Stoichometry(Y, N)?")
i = input()
if i == 'Y':
    s = Stoichometry(None)
    s.main()
else:
    s = Stoichometry(None)
