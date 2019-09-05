##Nathan Hinton
##This program is for converting between differing measurement systems.

def enterInformation():
    start = input('Current system of measurement: ')
    end = input('Goal system of measurement: ')
    distance = input('Distance: ')
    return start, end, distance

#Here is the state machine that will process the data:
state = 'init'
while start != 'end':
    if state == 'init':
        start, end, measure = enterInformation()
        state = 'findStart'
    
    else:
        print('ERROR IN STATEMACHINE FOR CONVERTING MEASUREMENTS!')
##Here is testing for the program:
print(enterInformation())
