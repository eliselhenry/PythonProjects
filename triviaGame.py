# Trivia Game: Questions Class
# Elise Henry (Driver) - U57226177
# Joceline Rios (Navigator) - U40591531
# This module contains the class definition.

class Question:
    def __init__(self, question, ans1, ans2, ans3, ans4, correct_idx):
        self.question = question
        self.answer1 = ans1
        self.answer2 = ans2
        self.answer3 = ans3
        self.answer4 = ans4
        self.correct_ans = correct_idx

    def __str__(self):
        print_str = ''
        print_str += self.question + '\n'
        print_str += '1. ' + self.answer1 + '\n'
        print_str += '2. ' + self.answer2 + '\n'
        print_str += '3. ' + self.answer3 + '\n'
        print_str += '4. ' + self.answer4

        return print_str
