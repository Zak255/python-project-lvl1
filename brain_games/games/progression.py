# !/usr/bin/env python
from random import randint
from brain_games.cli import *


DESCRIPTION = 'What number is missing in the progression?'


def question_and_correct_answer():
    random_number1 = randint(1, 10)
    random_number2 = randint(70, 100)
    step = randint(5, 10)
    random_list = list(range(random_number1, random_number2, step))
    index = randint(1, len(random_list) - 1)
    correct_answer = random_list[index]
    random_list[index] = '..'
    new_str = (' '.join(map(str, random_list)))
    question = new_str
    return question, str(correct_answer)


1
