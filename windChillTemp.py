# Elise Henry (Driver) U57226177
# Matthew Sharp (Navigator) U55969255
# Write a program that asks the user to enter a temperature between -58 degrees Fahrenheit and 41 degrees Fahrenheit.
# The program then calculates the wind-chill temperature using the formula above. Format the output to 3 decimal places.

temp = int(input("Enter a temperature between -58 degrees Fahrenheit and 41 degrees Fahrenheit: "))
while temp > 41 or temp < -58:
    print("Temperature must be between -58F and 41F")
    temp = int(input("Please re-enter the temperature in Fahrenheit: "))
wind_speed = int(input("Enter the wind speed in mph: "))
while wind_speed <= 2:
    print("Wind speed must be greater than or equal to 2mph.")
    wind_speed = int(input("Please re-enter the wind speed in mph: "))

wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * (temp * (wind_speed ** 0.16)))

print("The windchill index is {:.3f}".format(wind_chill))
