#Nathan Hinton
#11/13/2018
#Main program for python school

#Import files:
mode = 'direct'
print()
print("NO AUTORUNNING IF IN DIRECT MODE!")
print("Mode: "+mode)
print()

#mode = 'indirect'#Un comment to change the mode.
if mode == 'direct':
    from StateMachines import StateMachines as SMF
    from Science import Stoichometry as S
else:
    from StateMachines import StateMachines as SMF
    from Science import MainV2

#init classes:

Stoi = S.Stoichometry(mode)
print("Options setup:")
print("Stoi = Science/Stoichometry.py")

