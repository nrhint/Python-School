def area():
    print("Slant height does with depth.")
    w = int(input("Width:  "))
    d = int(input("Depth:  "))
    h = int(input("Height:  "))
    sh = int(input("Slant height:  "))
    print(h*d+sh*d+w*d+w*h)
def volume():
    w = int(input("Width:  "))
    d = int(input("Depth:  "))
    h = int(input("Height:  "))
    print((w*d)*h)
def help():
    print("NEEDS WORK")

def run():
    print("1:area")
    print("2:volume")
    i = input()
    if i == '1':
        area()
    elif i == '2':
        volume()
    else:
        print("Invalis Input")

print("Done loading Prism programs.  May need help.  Be careful using this portion.")
