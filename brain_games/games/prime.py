# !/usr/bin/env python
from random import randint


number = randint(2, 20)


def welcome_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


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
    correct_answer = ''
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def logic_user():
    user_name = ''
    user_name = input("My I have your name?  ")
    print(f"Hello, {user_name.capitalize()}!")
    curcle = 0

    for _ in range(0, 3):
        question, correct_answer = make_question()
        print('Question: {}'.format(question))
        answer = input("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
            curcle += 1

        else:
            right_answer = answer != correct_answer
            print(
                f"'{answer}' is wrong answer :(.\nCorrect answer was '{correct_answer}'.\nLet\'s try again, {user_name}!")
            break

    if curcle == 3:
        print(f'Congratulations, {user_name.capitalize()}!')
