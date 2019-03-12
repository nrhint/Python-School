def area():
    r = input("Radius:  ")
    print(4 * 3.14 * int(r) ** 2)
def volume():
    r = input("Radius:  ")
    print((4/3) * 3.14 * int(r) ** 3)
def help():
    print("""
No help for this module.

Area and Volume are defined.
""")

def run():
    print("1:area")
    print("2:volume")
    i = input()
    if i == '1':
        area()
    elif i == '2':
        volume()
    else:
        print("Invalid input")

print("Done loading Sphere Programs")
