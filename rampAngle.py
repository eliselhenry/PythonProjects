# Elise Henry (Driver) U57226177
# Matthew Sharp (Navigator) U55969255
# A program that prompts the user to enter the Force and mass of a cart to get the angle of a ramp

import math
import constant
pi = 3.14
Gravity = 9.8
math.degrees


m = int(input("Enter mass of the cart (in kg): "))
force = int(input("Enter the force of the cart (in N): "))

x = math.asin(force/(m * Gravity))
degrees = x * (180/pi)

print("The angle of the ramp is {:.1f} degrees".format(degrees))
