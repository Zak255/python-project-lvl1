from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def question_and_correct_answer():
    random_number1 = randint(1, 10)
    random_number2 = randint(70, 100)
    step = randint(5, 10)
    random_list = list(range(random_number1, random_number2, step))
    index = randint(1, len(random_list) - 1)
    correct_answer = random_list[index]
    random_list[index] = '..'
    question = (' '.join(map(str, random_list)))
    return question, str(correct_answer)
