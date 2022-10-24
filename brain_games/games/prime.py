# !/usr/bin/env python
from random import randint


def welcome_prime():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name.capitalize()}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number = randint(2, 20)
    print("Questions: {}".format(number))
    answer = input("Your answer: ")

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True

def make_question():
    """Make game question and answer."""
    number = randint(2, 20)
    question = str(number)
    return question, is_prime(number)