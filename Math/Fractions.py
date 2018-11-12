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
            self.t = int(self.T1)*int(self.B2)
            self.b = int(self.B1)*int(self.T2)

        print(str(self.t) + " / " + str(self.b))

        while smaller == False:
            x = x+1
            if self.b%x == 0 and self.t%x == 0:
                self.t = self.t/x
                self.b = self.b/x
                print(str(self.t) + " / " + str(self.b))
                x = 1
            if x >= self.b:
                smaller = True

print("Done loading Fraction programms")
print("!!!THIS PROGRAM HAS BEEN CONVERTED INTO A CLASS! IT MAY NOT FUNCTION IN OLDER PROGRAMS!!!")
