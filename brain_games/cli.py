#!/usr/bin/env python3
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name.capitalize()}")
    return name


def correct_answer_massage(user_answer, correct_answer, name):
    print(
        f"'{user_answer.capitalize()}' is wrong answer :(."
        f"\nCorrect answer was '{correct_answer.capitalize()}'."
        f"\nLet\'s try again, {name.capitalize()}!")


if __name__ == '__main__':
    welcome_user()
    correct_answer_massage()
