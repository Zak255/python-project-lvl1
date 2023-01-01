# !/usr/bin/env python
from random import randint
from brain_games.cli import *


DESCRIPTION = 'Answer "yes" if given number is prime.'\
    'Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return "no"
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return "no"
    return "yes"


def question_and_correct_answer():
    number = randint(2, 20)
    question = str(number)
    return question, is_prime(number)
