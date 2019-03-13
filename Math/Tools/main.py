#Nathan Hinton
#This program will contain tools for working with distances and temps.

def temp():#V1
    temp = float(input("Temprature: "))
    to = input("Convert to (C, F): ")
    if to == 'C' or to == 'c':
        print(round((temp-32)/1.8, 2))
    elif to == 'F' or to == 'f':
        print(round(temp*1.8+32, 2))
    else:
        print("Invalid Input")

def meteric():
    l = ['u' 'mm', 'd', 'm', 'M', 'k', 'c']
    dist = float(input("Distance: "))
    curr = str(input("Current meteric: "))
    to = str(input("Convert to: "))
    if to == 'cm':
        pass
    
