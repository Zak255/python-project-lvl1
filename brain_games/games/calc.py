from random import randint
import random


DESCRIPTION = 'What is the result of the expression?'


def question_and_correct_answer():
    random_number1 = randint(0, 20)
    random_number2 = randint(1, 18)
    value = ['+', '-', '*']
    value_answer = random.choice(value)
    question = '{} {} {}'.format(random_number1, value_answer, random_number2)
    correct_answer = eval(f'{random_number1} {value_answer} {random_number2}')
    return question, str(correct_answer)
