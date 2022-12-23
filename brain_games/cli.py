#!/usr/bin/env python
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    return name


def get_answer(question):
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ")
    return answer


def correct_answer_massage(answer, right_answer, name):
    print("""'{}' is wrong answer ;(.
    Correct answer is '{}'.".format(answer, right_answer, name)""")
    print("Let's try again, {}!".format(name))
