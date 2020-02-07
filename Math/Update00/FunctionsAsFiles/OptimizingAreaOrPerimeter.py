##Nathan Hinton
##Optimizing an area or perimeter

lengths = [5, 6, 7]
perimeter = 28
area = 100

for x in lengths:
    print()
    print("Perimeters: %s, %s" %(x, (perimeter/2)-x))
    print("Area: %s" %(x*((perimeter/2)-x)))

print()
print()
print()
for x in lengths:
    print()
    print("Missing length: %s"%(area/x))
    print("Perimeter: %s"%(((area/x)+x)*2))
    
