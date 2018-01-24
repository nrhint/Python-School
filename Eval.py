import math as m

def Eval():
    print("math is m")
    print("Answers are rounded to the ten millionth")
    E1 = input("Equation1:  ")
    E2 = input("Equation1:  ")
    
    if round(int(E1), 10) == round(int(E2), 10):
        print("Equal")
    else:
        print("Not Equal")
print("Done Loading Eval program")
