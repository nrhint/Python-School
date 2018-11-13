#Nathan Hinton
#11/13/2018
#For plotting points

class Graph:
    def __init__(self):
        print("Class Graph inited")
        print("Y=mX+b")
        self.m = 0
    def inp(self):
        self.x = int(input("x1: "))
        self.y = int(input("y1: "))
        self.set1 = (self.x, self.y)
        self.x = int(input("x2: "))
        self.y = int(input("y2: "))
        self.set2 = (self.x, self.y)
        self.m = 0
    def calcM(self):
        self.inp()
        self.m = (self.set1[0]-self.set2[0])/(self.set1[1]-self.set2[1])
        print()
        print(self.m)
    def calcB(self):
        if self.m == 0:
            self.calcM()
        #Y+mX+b
        self.b = self.y - self.m*self.x
        print()
        print(self.b)
        print(str(self.y) + '=' + str(self.m) + '*' + str(self.x) + '+' + str(self.b))

#Autorun:
g = Graph()
g.calcM()
