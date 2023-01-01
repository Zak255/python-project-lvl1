import prompt
from brain_games.cli import *


def run_game(game_name):
    name = welcome_user()
    print(game_name.DESCRIPTION)
    curcle = 0
    for _ in range(0, 3):
        question, correct_answer = game_name.question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if not (user_answer == correct_answer):
            return correct_answer_massage(user_answer, correct_answer, name)

        print("Correct!")
        curcle += 1
    if curcle == 3:
        print(f"Congratulations {name.capitalize()}")
