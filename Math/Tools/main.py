#Nathan Hinton
#This program will contain tools for working with distances and temps.

def temp():
    temp = int(input("Temprature: "))
    to = input("Convert to (C, F): ")
    if to == 'C' or to == 'c':
        print(temp*1.8+32)
    elif to == 'F' or to == 'f':
        print(temp/1.8-32)
    else:
        print("Invalid Input")
