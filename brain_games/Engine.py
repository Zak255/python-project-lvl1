import prompt
from brain_games.cli import welcome_user


def run_game(game_name):
    name = welcome_user()
    print(game_name.DESCRIPTION)
    curcle = 0
    for _ in range(0, 3):
        question, correct_answer = game_name.question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if not (user_answer == correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {name.capitalize()}!")
            break
        print("Correct!")
        curcle += 1
    if curcle == 3:
        print(f"Congratulations, {name.capitalize()}!")
