# Elise Henry
# Task at hand is to prompt the user to enter a numerator and denominator and
# calculate whether it's a proper or improper fraction, if it can be reduced,
# and the mixed and/or whole number from that fraction.

import math

a = int(input("Enter a numerator (value must be greater than 0): "))
while a < 0 or a == 0:
    print("Numerator value must be greater than 0. ")
    a = int(input("Please re-enter the numerator: "))
b = int(input("Enter a denominator (value must be greater than 0): "))
while b < 0 or b == 0:
    print("Denominator value must be greater than 0. ")
    b = int(input("Please re-enter the denominator: "))

math.gcd(a, b)
a2 = a // b
b2 = a % b

if a < b or a == b:
    print(a, '/', b, "is a proper fraction.")
    if math.gcd(a, b) != 1:
        print("This proper fraction can be reduced to: ", a // math.gcd(a, b), "/", b // math.gcd(a, b))
    else:
        print("This proper fraction cannot be reduced any further.")
else:
    print(a, '/', b, "is an improper fraction.")
    if math.gcd(a, b) != 1:
        print("This improper fraction can be reduced to: ", a // math.gcd(a, b), "/", b // math.gcd(a, b))
        if b2 == 0:
            print("The whole number is", a2)
        else:
            print('The mixed number is {} and {}/{}'.format(a2, b2, b))
    else:
        print("This improper fraction cannot be reduced any further.")
        if b2 == 0:
            print("The whole number is", a2)
        else:
            print('The mixed number is {} and {}/{}'.format(a2, b2, b))

