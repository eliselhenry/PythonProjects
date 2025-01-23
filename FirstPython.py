# Area of a Hexagon
# Write program that prompts user to enter side of a hexagon and displays its area.
# Format the result to three decimal places.

import math
side = float(input("Enter the side length of the hexagon: "))
area = float(((3* math.sqrt(3))/2)*(math.pow(side,2)))

print("The area of a hexagon with side length", side, "is {:.3f}.".format(area))
