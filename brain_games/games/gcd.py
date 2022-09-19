from random import randint
from math import gcd


def logic_gcd_game():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name.capitalize()}!")
    print('Find the greatest common divisor of given numbers.')

    for i in range(0, 3):
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        maths_answer = gcd(random_number1, random_number2)
        print("Questions : {} {}".format(random_number1, random_number2))
        answer = int(input())

        while maths_answer!= answer:
            if random_number1 > random_number2:
                random_number1 -= random_number2

            elif maths_answer == answer:
                print(f"Your answer : {answer}!")
                print("Correct !".format())
                break

            else:
                maths_answer != answer
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{maths_answer}'.Let\'s try again, {user_name.capitalize()} !")
                quit()

    print(f"Congratulations, {user_name.capitalize()}!")
logic_gcd_game()
