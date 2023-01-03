from random import choice, randint
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def question_and_correct_answer():
    random_number1 = randint(0, 20)
    random_number2 = randint(1, 18)
    operation, operator = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*'),
    ])
    correct_answer = operation(random_number1, random_number2)
    question = f'{random_number1} {operator} {random_number2}'
    return question, str(correct_answer)
