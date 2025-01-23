# Elise Henry (Driver) U57226177
# Francisco Lozoya (Navigator) U60053168
# A program that gathers the starting radius, offset, and number of circles from the user.
# Then uses the turtle function to draw colored circles.

import turtle

# radius of the circle
r = int(input("Enter a starting radius (must be >= 10): "))
while r < 10:
    r = int(input("Please re-enter a radius greater than or equal to 10: "))
# offset of the next circle
o = int(input("Enter a value to increase the radius of the next circle (must be >= 5): "))
while o < 5:
    o = int(input("Please re-enter a value greater than or equal to 5: "))
num_circles = int(input("Please enter the number of circles to draw. Must be at least 1: "))
while num_circles < 1:
    num_circles = int(input("Please re-enter a value greater than or equal to 1: "))
colors = ["red", "orange", "yellow", "green", "blue", "purple"] * num_circles

turtle.speed(10)
turtle.circle(r)

for circle in range(num_circles):
    turtle.color(colors[circle])
    turtle.circle(r + (circle * o))
    turtle.penup()
    turtle.sety(-r - circle * o)
    turtle.pendown()
