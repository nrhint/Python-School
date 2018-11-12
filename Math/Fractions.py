class Fraction:
    def __init__(self):
        print("Fraction Initing...")
    def run(self):
        smaller = False
        x = 1
        self.T1 = input("top of fraction 1:  ")
        self.B1 = input("bottom of fraction 1:  ")
        self.equ = input("equeator:  ")
        self.T2 = input("top of fraction 2:  ")
        self.B2 = input("bottom of fraction 1:  ")

        self.b = int(self.B2)*int(self.B1)
        self.t1 = int(self.B2)*int(self.T1)
        self.t2 = int(self.B1)*int(self.T2)

        print(str(self.t1) + " / " + str(self.b) + " " + self.equ + " " + str(self.t2) + " / " + str(self.b))

        if self.equ == '+':
            self.t = self.t1+self.t2
        elif self.equ == '-':
            self.t = self.t1-self.t2
        elif self.equ == '*':
            self.t = self.t1*self.t2
            self.b = self.b*self.b
        elif self.equ == '/':
            t = int(T1)*int(B2)
            b = int(B1)*int(T2)

        print(str(t) + " / " + str(b))

        while smaller == False:
            x = x+1
            if b%x == 0 and t%x == 0:
                t = t/x
                b = b/x
                print(str(t) + " / " + str(b))
                x = 1
            if x >= b:
                smaller = True

print("Done loading Fraction programms")
