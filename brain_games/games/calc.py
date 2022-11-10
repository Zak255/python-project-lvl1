# !/usr/bin/env python
from random import randint
import random


def is_calc_game():
    curcle = 0
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name.capitalize()}!")
    print('What is the result of the expression?')

    for i in range(0, 3):
        random_number1 = randint(0, 20)
        random_number2 = randint(1, 18)
        value = ['+', '-', '*']
        value_answer = random.choice(value)
        computer_question = f'{random_number1} {value_answer} {random_number2}'
        print('Question: {}'.format(computer_question))
        answer = int(input())
        correct_answer = False

        if answer == eval(computer_question):
            correct_answer = random_number1 + random_number2
            print("Your answer: {}".format(answer))
            print("Correct!")
            curcle += 1

        elif answer == eval(computer_question):
            correct_answer = random_number1 - random_number2
            print("Your answer: {}".format(answer))
            print("Correct!")
            curcle += 1

        elif answer == eval(computer_question):
            correct_answer = random_number1 * random_number2
            print("Your answer: {}".format(answer))
            print("Correct!")
            curcle += 1

        else:
            right_answer = f"{random_number1} {value_answer} {random_number2}"
            print(
                f"'{answer}' is wrong answer ;(."
                f"\nCorrect answer was '{eval(right_answer)}'."
                f"\nLet\'s try again, {user_name}!")
            break

    if curcle == 3:
        print(f"Congratulations, {user_name.capitalize()}!")
