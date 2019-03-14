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

def distanceMetric():
    units = {k:1000, M:1, dc:0.1, cm:0.01, m:0.001, u:0.000001, n:0.000000001, p:0.000000000001}
    dist = float(input("Distance: "))
    curr = str(input("Current meteric: "))
    to = str(input("Convert to: "))
    if to == 'cm':
        pass
    
