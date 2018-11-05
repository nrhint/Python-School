def area():
    base = input("base  ")
    height = input("height  ")
    print(int(base)*int(height))
def permiter():
    s1 = input("Side 1  ")
    s2 = input("Side 2  ")
    s3 = input("Side 3  ")
    s4 = input("Side 4  ")
    print(int(s1)+int(s2)+int(s3)+int(s4))

def help():
    print("Help for SQU set")
    print("""
The way that this was designed was to make it so you enter SQU and that stands
for Square, then you enter the first leters of what you want to do in caps
and after the last capital leter you put the next leter of the function an
lowercace.  Example: for the area of a square you put SQU with Ar for area
right after to make SQUAr.
    """)
    print()
    print("Here is a list of Square commands")
    print("""
SQU-------Show SQU help.
SQUAr-----Square area.
SQUPe-----Square calcluate the permiter of a triangle
    """)
##end SQU help

print("Done loading Square programms")
