from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_correct_answer():
    random_number = randint(1, 99)
    question = str(random_number)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
