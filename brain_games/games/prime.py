from random import randint


def logic_prime():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name.capitalize()}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for a in range(0, 3):

        random_number = randint(2, 10)
        print("Questions : {}".format(random_number))
        answer = input('Your answer: ')
        k = 0

        for a in range(2, random_number // 2 + 1):
            if random_number % a == 0:
                k += 1
        if k <= 0 and answer == "Yes":
            print('Correct Y!')

        elif k >= 0 and answer == "No":
            print('Correct N!')

        else:
            right_answer = "Yes" if answer != "Yes" else "No"
            print(f"'{answer.capitalize()}' is wrong answer :(. Correct answer was '{right_answer.capitalize()}'. Let\'s try again, {user_name.capitalize()}!")
            break
    else:
        print('Congratulation {}'.format(user_name.capitalize()))
logic_prime()