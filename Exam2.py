# Python Programming Exam 2
# Elise Henry
# Complex Number Calculator:
# A program that displays math operations, asks the user for a choice,
# then asks the user for two complex numbers.
# The program uses the complex() function to compute the result
# and repeats the process until the user says ‘no’.

def display_menu():
    print("\nWelcome to the Complex Number program!\n")
    print("Here are your choices:")
    print("1. Adding two complex numbers.")
    print("2. Subtracting two complex numbers.")
    print("3. Multiplying two complex numbers.")
    print("4. Dividing two complex numbers.")


def add_complex(z1, z2):
    return z1 + z2


def sub_complex(z1, z2):
    return z1 - z2


def mult_complex(z1, z2):
    return z1 * z2


def div_complex(z1, z2):
    return z1 / z2


while True:
    display_menu()
    user_choice = int(input("Enter your choice (1 to 4): "))
    while user_choice < 1 or user_choice > 4:
        print("This is an invalid option.")
        user_choice = int(input("Enter your choice (1 to 4): "))

    a1 = int(input("Enter the REAL part of the FIRST complex expression: "))
    a2 = int(input("Enter the IMAGINARY part of the FIRST complex expression: "))
    b1 = int(input("Enter the REAL part of the SECOND complex expression: "))
    b2 = int(input("Enter the IMAGINARY part of the SECOND complex expression: "))

    z1 = complex(a1, a2)
    z2 = complex(b1, b2)

    if user_choice == 1:
        print(z1, "+", z2, "is ", add_complex(z1, z2))
    elif user_choice == 2:
        print(z1, "-", z2, "is ", sub_complex(z1, z2))
    elif user_choice == 3:
        print(z1, "*", z2, "is ", mult_complex(z1, z2))
    elif user_choice == 4:
        print(z1, "/", z2, "is ", div_complex(z1, z2))
    run_again = input("\nWould you like to run the program again? Enter yes or no: ")
    if run_again == 'no':
        break
print("Thanks for using the program, goodbye!")
