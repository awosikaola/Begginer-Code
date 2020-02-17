#importing the math module

from math import sqrt

#user input the value for one side of the hexagon

square = int(input ("Enter the value for a side of the Hexagon: "))

#formula for calculating the area of a hexagon

area = ((3*sqrt(3))/2)*pow(square,2)

#print the output of the claculated area

print (area)

#exut the program

exit (input("Press any key to exit"))
