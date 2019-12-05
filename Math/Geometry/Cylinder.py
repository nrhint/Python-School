##Nathan Hinton

##TO DO##
## define a volume program
## define surface area
## 
##
##
##
##

def area():
    r = input("Radius:  ")
    h = input("Height:  ")
    p = 3.14  #Pi
    print(2*int(p)*int(r)**2+2*p*int(r)*int(h))
def volume():
    r = input("Radius:  ")
    h = input("Height:  ")
    p = 3.14  #Pi
    try:
        print(int(r)**2*p*int(h))
    except ValueError:
        print(float(r)**2*p*float(h))

def run():
    print("1:area")
    print("2:voume")
    i = input()
    if i == '1':
        area()
    elif i == '2':
        volume()
    else:
        print("Invalid input")

print("Done loading Cylinder programs")
