# !/usr/bin/env python
from random import randint
from math import gcd
from brain_games.cli import welcome_user


def logic_gcd_game():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    for i in range(0, 3):
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        maths_answer = gcd(random_number1, random_number2)
        print('Question: {} {}'.format(random_number1, random_number2))
        answer = int(input())

        while maths_answer != answer:
            if random_number1 > random_number2:
                random_number1 -= random_number2

            elif maths_answer == answer:
                print("Your answer: {}".format(answer))
                print("Correct!".format())
                break

            else:
                right_answer = maths_answer != answer
                print(
                    f"'{answer}' is wrong answer ;(."
                    f"\nCorrect answer was '{right_answer}'."
                    f"\nLet\'s try again, {name}!")
                quit()

        print(f"Congratulations, {name.capitalize()}!")
