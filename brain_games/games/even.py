# !/usr/bin/env python3
from random import randint


def is_even_game():
    curcle = 0
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name.capitalize()}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(0, 3):
        random_number = randint(0, 101)
        print('Question: {}'.format(random_number))
        answer = input()

        if random_number % 2 == 0 and answer.capitalize() == 'Yes':
            print(f"Your answer: {answer.capitalize()}!")
            print("Correct!".format(answer.capitalize()))
            curcle += 1

        elif random_number % 2 != 0 and answer.capitalize() == 'No':
            print(f"Your answer: {answer.capitalize()}!")
            print("Correct!".format(answer.capitalize()))
            curcle += 1

        else:
            right_answer = 'Yes' if random_number % 2 == 0 else 'No'
            print(f"'{answer.capitalize()}' is wrong answer :(.\nCorrect answer was '{right_answer.capitalize()}'.\nLet\'s try again, {user_name.capitalize()}!")
            break

    if curcle == 3:
        print(f"Congratulations, {user_name.capitalize()}!")