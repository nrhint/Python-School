##Nathan Hinton
##Using aleks math
##EXAMPLE:
##Here are the endpoints of a segment BC
##B(-6, 4), C(1, 2)
##find the exact length

from math import sqrt

####Here is the input section:
##b = (1, -8)
##c = (3, -1)
##
###set a to make a right triangle:
##a = (b[0], c[1])
##
##print("Rounded answer:")
##print(sqrt((b[1]-a[1])**2+(c[0]-a[0])**2))
##print()
##print("Exact answer:")
##print("sqrt("+str((b[1]-a[1])**2+(c[0]-a[0])**2)+")")

print("lengthOfLineGivenEndpoints returns the rounded answer and the equation used")
print()
def lengthOfLineGivenEndpoints(pointa, pointb):
    ##Here is the input section:
    b = pointa#(1, -8)
    c = pointb#(3, -1)

    #set a to make a right triangle:
    a = (b[0], c[1])

##    print("Rounded answer:")
##    print(sqrt((b[1]-a[1])**2+(c[0]-a[0])**2))
##    print()
##    print("Exact answer:")
##    print("sqrt("+str((b[1]-a[1])**2+(c[0]-a[0])**2)+")")
    return sqrt((b[1]-a[1])**2+(c[0]-a[0])**2), "sqrt(("+str(b[1]-a[1])+")**2+("+str(c[0]-a[0])+")**2)"
