def run():
    smaller = False
    x = 1
    T1 = input("top of fraction 1:  ")
    B1 = input("bottom of fraction 1:  ")
    equ = input("equeator:  ")
    T2 = input("top of fraction 2:  ")
    B2 = input("bottom of fraction 1:  ")

    b = int(B2)*int(B1)
    t1 = int(B2)*int(T1)
    t2 = int(B1)*int(T2)

    print(str(t1) + " / " + str(b) + " " + equ + " " + str(t2) + " / " + str(b))

    if equ == '+':
        t = t1+t2
    elif equ == '-':
        t = t1-t2
    elif equ == '*':
        t = t1*t2
        b = b*b
    elif equ == '/':
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
