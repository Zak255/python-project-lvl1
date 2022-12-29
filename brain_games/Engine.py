from brain_games.cli import *
import prompt
from brain_games.games.even import question_and_correct_answer, description


def run_game():
    name = welcome_user()
    print(description)
    curcle = 0
    for _ in range(0, 3):
        question, answer = question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answewr: ")
        if user_answer.capitalize() != answer:
            return correct_answer_massage(answer.capitalize(), user_answer.capitalize(), name.capitalize())
        print("Correct!")
        curcle += 1
    if curcle == 3:
        print(f"Congratulations {name.capitalize()}!")


print(run_game())
