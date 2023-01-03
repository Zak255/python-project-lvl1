import prompt
from brain_games.cli import welcome_user


def run_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    curcle = 0
    for _ in range(0, 3):
        question, correct_answer = game.question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            curcle += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {name}!")
            break

    if curcle == 3:
        print(f"Congratulations, {name}!")
