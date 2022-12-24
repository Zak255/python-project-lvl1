# !/usr/bin/env python
from random import randint
from brain_games.cli import welcome_user, get_answer, answers,correct_answer_massage

discription = 'Answer "yes" if the number is even, otherwise answer "no".'

def even_game():
    rounds = 0
    name = welcome_user()
    print(discription)

    for i in range(0, 3):
        questions = get_answer(randint(0, 101))
        user_answer = answers()
        if questions % 2 == 0 and user_answer.capitalize() == "Yes":
            print("Correct!")
            rounds += 1
        elif questions % 2 != 0 and user_answer.capitalize() == "No":
            print("Correct!")
            rounds += 1
        else:
            right_answer = 'Yes' if questions % 2 == 0 else 'No'
            return correct_answer_massage(user_answer,right_answer,name)

    if rounds == 3:
        print("Congratulations {}".format(name.capitalize()))        
even_game()
