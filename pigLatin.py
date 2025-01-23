# COP2510 Assignment 6 Part 1
# Michael Alexander (U62660400) and Elise Henry(U57226177)
# Driver: Michael
# Navigator: Elise
# Participation: 50/50
# Description: The concept of this program is to create a code that converts any text into Pig Latin language.

def pig_Latin(input_file):
    output_file_name = input("Enter the output file name: ")
    output_file_name = output_file_name + ".txt"
    output_file = open(output_file_name, "a")
    for line in input_file:
        for word in line.split():
            if len(word) != 1:
                word = word[1:] + word[0] + "ay"
                output_file.write(" " + word)

            else:
                word = word + "ay"
                output_file.write(" " + word)
    output_file.close()

    return output_file


if __name__ == '__main__':
    input_file_name = input("Enter the name of your input file: ")
    try:
        input_file = open(input_file_name, 'r')
        output_file = pig_Latin(input_file)
        print(output_file)
    except IOError:
        print("Could not find the file:", input_file_name)
