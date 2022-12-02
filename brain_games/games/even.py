# !/usr/bin/env python
from random import randint
from brain_games.cli import welcome_user


def is_even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    curcle = 0

    for i in range(0, 3):
        random_number = randint(0, 101)
        print('Question: {}'.format(random_number))
        answer = input()

        if random_number % 2 == 0 and answer.capitalize() == 'Yes':
            print("Your answer: {}".format(answer.capitalize()))
            print("Correct!")
            curcle += 1

        elif random_number % 2 != 0 and answer.capitalize() == 'No':
            print("Your answer: {}".format(answer.capitalize()))
            print("Correct!")
            curcle += 1

        else:
            right_answer = 'Yes' if random_number % 2 == 0 else 'No'
            print(
                f"'{answer}' is wrong answer :(."
                f"\nCorrect answer was '{right_answer}'."
                f"\nLet\'s try again, {name}!")
            break

    if curcle == 3:
        print(f"Congratulations, {name.capitalize()}!")
