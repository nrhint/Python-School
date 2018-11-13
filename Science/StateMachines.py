#Nathan Hinton
#11/13/2018
#State machines

#Errors for the machines:
class StateMachineError(Exception):
    pass

#State machines.
class ProcessInput:
    def __init__(self):
        print("Class ProcessInput created")
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
                else:
                    raise StateMachineError("@ Digit expected upper or digit", state)
            else:
                raise StateMachineError("@StateMachine expected something, I dont know what", state)
        commit()
        return self.finalData
