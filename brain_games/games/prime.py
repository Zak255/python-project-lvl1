from random import randint
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number + 1))):
        if number % i == 0:
            return False
    return True


def question_and_correct_answer():
    number = randint(1, 99)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
