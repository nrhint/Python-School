def area():
    w = int(input("Width:  "))
    h = int(input("Height:  "))
    d = int(input("Depth:  "))
    print(((h*w)+(w*d)+(d*h))*2)
def volume():
    w = int(input("Width:  "))
    h = int(input("Height:  "))
    d = int(input("Depth:  "))
    print(w*h*d)
def permiter():
    w = int(input("Width:  "))
    h = int(input("Height:  "))
    d = int(input("Depth:  "))
    print((w*4)+(d*4)+(h*4))
def help():
    print("Help for CUB set")
    print("""
The way that this was designed was to make it so you enter CUB and that stands
for Cuboid, then you enter the first leters of what you want to do in caps
and after the last capital leter you put the next leter of the function an
lowercace.  Example: for the area of a cuboid you put CUB with Ar for area
right after to make CUBAr.
    """)
    print()
    print("Here is a list of Cuboid commands")
    print("""
CUB-------Show CUB help.
CUBVo-----Cuboid volume.
CUBAr-----Cuboid area.
CUBPe-----Cuboid calcluate the total edge length of a square--Not sure why thisis here.
    """)
##end CUB help

def run():
    print("1:area")
    print("2:volume")
    print("3:perimeter")
    i = input()
    if i == '1':
        area()
    elif i == '2':
        volume()
    elif i == '3':
        permiter()
    else:
        print("Invalid input")

print("Done loading Cuboid programms")

"""
w = width
h = height
d = depth

volume: w*l*h
TSA: (h*w)*(w*d)*(d*h)*2
Permiter: (w*4)+(d*4)+(h*4)
"""
