# !/usr/bin/env python
from random import randint
import prompt

def logic_progression():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name.capitalize()}!")
    print('What number is missing in the progression?')
    curcle = 0
    random_list = []

    for i in range(0, 3):
        random_number1 = randint(1, 10)
        random_number2 = randint(70, 100)
        step = randint(5, 10)
        random_list = list(range(random_number1, random_number2, step))
        index = randint(1,len(random_list) -1)
        correct_answer = random_list[index]
        random_list[index] = '..'
        new_str = (' '.join(map(str, random_list)))
        print('Question: {}'.format(new_str))
        answer = int(input())

        if answer == correct_answer:
            print('Your answer: {}'.format(answer))
            print('Correct!')
            curcle += 1

        else:
            right_answer = correct_answer != answer
            print(f"'{answer}' is wrong answer ;(.\nCorrect answer was '{right_answer}'.\nLet's try again, {user_name}!")
            break

    if curcle == 3:
        print(f"Congratulations, {user_name.capitalize()}!")