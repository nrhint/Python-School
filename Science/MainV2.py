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
class Science:
#########################Stuff to use for later input and data#################
    def __init__(self):#Version 1 unknown
        #Load the file as eleList
        print("Loading Element File")
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

    def amu(self, eleAbbr):#Version 1 unknown
        self.ele = self.findAtom(eleAbbr)
        self.ele = PD(self.ele)
        return self.ele[3]    
#REMOVED stoi and stoi2 and limitReagent and SearchAtom
    def Seperate(self, lst, item):#Version 1 unknown
        x = self.eleList[lst]
        try:
            return x[item]
        except IndexError:
            print("INDEX ERROR, something went wrong with you input")

    def PC(self):#Version 1 unknown
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
        self.number = 1
        self.finalData = []
        def commit():
            for l in range(int(self.number)):
                self.finalData.append(self.element)
            self.number = 1
            self.element = ''

        for x in self.i:
            print(state)
            if state == 'init':
                if x.isupper():
                    self.element += x
                    state = 'upper'
                else:
                    raise StateMachineError("@ init expected upper char", state)
            elif state == 'upper':#Done
                if x.isupper():
                    commit()
                    self.element += x
                elif x.islower():
                    self.element += x
                    state = 'lower'
                elif x.isdigit():
                    self.number = x
                    state = 'digit'
                else:
                    raise StateMachineError("@ upper unexpected char", state)
            elif state == 'lower':
                if x.isupper():
                    commit()
                    self.element += x
                    state = 'upper'
                elif x.isdigit():
                    self.number += x
                    state = 'digit'
                else:
                    raise StateMachineError("@ lower expected upper or digit", state)
            elif state == 'digit':
                if x.isupper():
                    commit()
                    self.element += x
                    state = 'upper'
                elif x.isdigit():
                    self.number += x
                    state = 'digit'
                else:
                    raise StateMachineError("@ Digit expected upper or digit", state)
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
        return self.inpDat
#    def inpNums(self):
#        self.inpDatNum = int(input("two or three numbers, seperate with spaces.  a 0 is a placeholder:  "))
#        return self.inp DatNum.split(' ')

#TO MAKE: STOICHOMETRY, 

################################################################################

s = Science()
S = Science()
#Science.main(self)
