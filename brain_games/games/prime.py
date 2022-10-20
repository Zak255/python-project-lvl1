# !/usr/bin/env python
import numbers
from random import randint


def welcome_prime():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name.capitalize()}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

def is_prime(number):
    print("Questions: {}".format(number))
    answer = input("Your answer: ")
    if number == 1:
        return "no"
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return "no"
    return "yes"

def make_question():
    """Make game question and answer."""
    min_number = 1
    max_number = 21
    number = randint(min_number, max_number)
    question = str(number)
    return question, is_prime(number)
