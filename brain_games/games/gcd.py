from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def question_and_correct_answer():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = f'{random_number1} {random_number2}'
    correct_answer = gcd(random_number1, random_number2)
    return question, str(correct_answer)


1
