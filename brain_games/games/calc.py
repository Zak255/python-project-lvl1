# !/usr/bin/env python
from random import randint
import random
from brain_games.cli import welcome_user


def logic_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    curcle = 0
    for i in range(0, 3):
        random_number1 = randint(0, 20)
        random_number2 = randint(1, 18)
        value = ['+', '-', '*']
        value_answer = random.choice(value)
        computer_question = f'{random_number1} {value_answer} {random_number2}'
        print('Question: {}'.format(computer_question))
        answer = int(input())

        if answer == eval(computer_question):
            random_number1 + random_number2
            print("Your answer: {}".format(answer))
            print("Correct!")
            curcle += 1

        elif answer == eval(computer_question):
            random_number1 - random_number2
            print("Your answer: {}".format(answer))
            print("Correct!")
            curcle += 1

        elif answer == eval(computer_question):
            random_number1 * random_number2
            print("Your answer: {}".format(answer))
            print("Correct!")
            curcle += 1

        else:
            right_answer = f"{random_number1} {value_answer} {random_number2}"
            print(
                f"'{answer}' is wrong answer ;(."
                f"\nCorrect answer was '{eval(right_answer)}'."
                f"\nLet\'s try again, {name}!")
            break

    if curcle == 3:
        print(f"Congratulations, {name.capitalize()}!")
