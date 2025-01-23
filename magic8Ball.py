# Elise Henry (Driver) U57226177
# Alisha Corbin (Navigator) U12534138
# MAGIC 8 BALL
# A program that prompts the user for a question and gives a random response from the 20 answers stored in the list.
# Includes two functions, a main function and a function that prints the response.
# Uses a while loop to continue or end the program based on the users decision.

import random


def main():
    print("Welcome to the Magic 8 Ball!")

    responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes-definitely.", "You may rely on it.",
                 "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                 "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                 "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
                 "Outlook not so good.", "Very doubtful."]

    while True:
        input("\nWhat is your question? ")
        rand_int = int(random.random() * 20)
        print(responses[rand_int])

        go_again = input("\nWould you like to ask another question? ")
        if go_again[0].lower() == "n":
            break
    print("\nGoodbye!")


if __name__ == "__main__":
    main()

