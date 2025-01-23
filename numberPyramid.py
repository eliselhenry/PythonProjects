# Elise Henry (Driver) U57226177
# Francisco Lozoya (Navigator) U60053168
# Number Pyramid: Program that prompts the user to enter a number between 1 and 9.
# The program should then display the numbers in a pattern. Use nested loops for this process.

lines = int(input("Enter the number of lines (must be between 1 and 9): "))
while lines < 1 or lines > 9:
    lines = int(input("Invalid number of lines. Re-enter a number between 1 and 9 (inclusive): "))
for i in range(1, lines+1):
    for j in range(1, lines-i+1):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i+1):
        print(j, end=" ")
    print()
