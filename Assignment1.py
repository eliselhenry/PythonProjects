# Prompt the user to enter speed and acceleration
# Calculate and display the runway length
# Format to four decimal places

speed = float(input("Enter speed in meters per second: "))
acceleration = float(input("Enter acceleration in meter per second squared: "))
runway_length = float((speed*speed)/(acceleration*2))

print("The minimum runway length is {:.4f}." .format(runway_length))
