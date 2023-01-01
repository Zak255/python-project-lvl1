from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_correct_answer():
    min_number = 1
    max_number = 99
    number = randint(min_number, max_number)
    question = str(number)
    if number % 2 == 0:
        correct_answer = 'Yes'
    else:
        correct_answer = 'No'
    return question, correct_answer
