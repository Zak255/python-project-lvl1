# !/usr/bin/env python
from random import randint


def welcome_prime():
    global user_name
    print("My I have your name?")
    user_name = input()
    print(f"Hello, {user_name.capitalize()}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number = randint(2, 20)

def is_prime(number):
    if number == 1:
        return False  
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True

def make_question():
    """Make game question and answer."""
    number = randint(2, 20)
    question = str(number)
    correct_answer = ''

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

def logic_user():
    curcle = 0
    for _ in range(0, 3):
        question, correct_answer = make_question()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer == correct_answer:
            print("Correct !")
            curcle +=1
        elif answer != correct_answer:
            print(
f''''{answer.capitalize()}' is wrong answer :(.
Correct answer was '{correct_answer.capitalize()}'.Let\'s try again, {user_name.capitalize()}!" ''')
            break
    if curcle == 3:
        print(f'Congratulations: {user_name.capitalize()}!')

if __name__ == '__main__':
    welcome_prime()
    is_prime(2)
    make_question()
    logic_user()
