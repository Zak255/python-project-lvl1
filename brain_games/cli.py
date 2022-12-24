#!/usr/bin/env python
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    return name


def get_answer(question):
    print(f"Question: {question}")
    return question


def answers():
    answer = prompt.string("Your answer: ")
    return answer


def correct_answer_massage(answer, right_answer, name):
    print(
        f"'{answer}' is wrong answer :(."
        f"\nCorrect answer was '{right_answer}'."
        f"\nLet\'s try again, {name}!")
