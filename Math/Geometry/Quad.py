class Square:
    def __init__(self):
        print("Square Init")
    def area(self):
        self.base = input("base  ")
        self.height = input("height  ")
        print(int(self.base)*int(self.height))
    def permiter(self):
        self.s1 = input("Side 1  ")
        print(int(self.s1)*4)

    def help(self):
        print("Help for SQU set")
        print()
        print("Here is a list of Square commands")
        print("""
    self.help-------Show Square help.
    self.area-------Square area.
    self.permiter---Square calcluate the permiter of a triangle
        """)

class Rectangle:
    def __init__(self):
        print("Rectangle Init")
    def area(self):
        self.base = input("base  ")
        self.height = input("height  ")
        print(int(self.base)*int(self.height))
    def permiter(self):
        self.s1 = input("Side 1  ")
        self.s2 = input("Side 2  ")
        print(int(self.s1)+int(self.s2)+int(self.s1)+int(self.s2))

    def help(self):
        print("Help for Rectangle class:")
        print()
        print("Here is a list of Rectangle commands")
        print("""
    self.help-------Rectangle help.
    self.area-------Rectangle area.
    self.permiter---Rectangle permiter.
        """)

class Quad:
    def __init__(self):
        print("THIS IS A BLANK CLASS TO BE DEVELOPED!!!")

print("Done loading Quad programms")
print("!!!THIS PROGRAM HAS BEEN CONVERTED INTO A CLASS! IT MAY NOT FUNCTION IN OLDER PROGRAMS!!!")
