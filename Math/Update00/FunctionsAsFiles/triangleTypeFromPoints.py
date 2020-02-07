##Nathan Hinton
##This is for taking 3 points and telling you what type of triangle it is

from lengthOfLineGivenEndpoints import *

points = ((0, 0), (0, 100), (87, 50))

a = lengthOfLineGivenEndpoints(points[0], points[1])
b = lengthOfLineGivenEndpoints(points[1], points[2])
c = lengthOfLineGivenEndpoints(points[2], points[0])

print("The lengths of the sides are:")
print(a[0])
print(b[0])
print(c[0])

def test(points):
    a = lengthOfLineGivenEndpoints(points[0], points[1])
    b = lengthOfLineGivenEndpoints(points[1], points[2])
    c = lengthOfLineGivenEndpoints(points[2], points[0])

    print("The lengths of the sides are:")
    print(a[0])
    print(b[0])
    print(c[0])

