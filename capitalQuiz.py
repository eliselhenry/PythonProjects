# Elise Henry (Driver) U57226177
# Alisha Corbin (Navigator) U12534138
# STATE CAPITALS QUIZ
# A program that quizzes the users on their knowledge of state capitals.
# Uses dictionary to store the states and their capitals as key value pairs.
# While loop to continue and stop the game is the users wants to.


import random

global states, capitals, correct, incorrect, used


def main():
    game_setup()
    play_game()


def game_setup():
    global states, capitals, correct, incorrect, used
    correct = 0
    incorrect = 0
    used = [False] * 50
    states = setup_states_list()
    capitals = setup_capitals_dictionary()
    print("The State Capitals Quiz!\n")


def play_game():
    global correct, incorrect, used
    guess = ""
    while guess.lower() != "quit":
        num = random.randint(0, len(states) - 1)
        while used[num]:
            num = random.randint(0, len(states) - 1)
        used[num] = True
        all_true = True
        for i in range(0, 50):
            if not used[i]:
                all_true = False
        if all_true:
            used = [False] * 50
        state = states[num]
        capital = capitals[state]
        guess = input("What is the capital of " + state + "? (or enter 'q' to quit): ")
        if guess.lower() == "q":
            print("\nYou had {0} correct responses and {1} incorrect responses.\nGoodbye!".format(correct, incorrect))
            break
        elif guess.lower() == capital.lower():
            print("That is correct! {0} is the capital of {1}.\n".format(capital, state))
            correct += 1
        else:
            print("Sorry, that is incorrect, the capital of {0} is {1}.\n".format(state, capital))
            incorrect += 1


def setup_states_list():
    return ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
            'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
            'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
            'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
            'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
            'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


def setup_capitals_dictionary():
    return {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California':
            'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
            'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana':
            'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana':
            'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey':
            'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota':
            'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania':
            'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia':
            'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming':
            'Cheyenne'}


main()
