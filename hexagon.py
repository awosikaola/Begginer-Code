from math import sqrt

def areaofhex(square):
    
    area = ((3*sqrt(3))/2)*pow(square,2)

    return area

square = int(input ("Enter side of the hexagon: "))

print (areaofhex(square))

