##Nathan Hinton
##This will return the surface area of a cylinder.

pi = 3.14

def surfaceAreaOfCylinder(r, height):
    approxArea = (r**2+r**2+(r*height)*2)*pi
    exactArea = ('%s*pi'%((r**2+r**2+(r*height)*2)))
    return (approxArea, exactArea)
