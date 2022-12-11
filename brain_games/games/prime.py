# !/usr/bin/env python
from random import randint
from brain_games.cli import welcome_user


number = randint(2, 20)


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True


def make_question():
    number = randint(2, 20)
    question = str(number)
    right_answer = ''
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


def logic_user():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    curcle = 0

    for _ in range(0, 3):
        question, right_answer = make_question()
        print('Question: {}'.format(question))
        answer = input("Your answer: ")

        if answer == right_answer:
            print("Correct!")
            curcle += 1

        else:
            print(
                f"'{answer}' is wrong answer :(."
                f"\nCorrect answer was '{right_answer}'."
                f"\nLet\'s try again, {name}!")
            break

    if curcle == 3:
        print(f'Congratulations, {name.capitalize()}!')
