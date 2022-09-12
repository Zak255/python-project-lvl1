# import random


# print("Welcome to the Brain Games!")
# user_name = input("May I have your name? ")
# print(f"Hello, {user_name}!")
# print('Answer "yes" if the number is even, otherwise answer "no".')
# count = 0
# num = random.randint(1, 100)
# for num in range(count):
#     question, correct_answer % 2 == 0
#     print("Question: {}".format(question))
#     user_answer = input("Your answer : ")
#     if correct_answer == user_answer:
#         print("Correct!")

# name = 'Tirion'
# print(name.upper().lower())

# name = 'Tirion'
# print(name[1:5].upper().find('I'))

# def print_motto():
#     message = input()
#     fix_message = message.strip()
#     result_fix = fix_message.lower()
# print(print_motto())


# def run():
#     return 5
#     return 10
# print(run())

# def password_case(password):
#     lenght = len(password)
#     return lenght > 8 and lenght < 20
# print(password_case('qwee'))



# def years_age(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
# print(years_age(2024))


# number = int(input())
# print(number % 2 == 0 and 'yes' or 'no')


# value == 'first' or value == 'second'
# print(value)

# def string_or_not(text):
#     return isinstance(text, str) and 'yes' or 'no'
# print(string_or_not('ddg'))

# from random import randint, random

# print("Welcome to the Brain Games!")
# user_name = input("May I have your name? ")
# print(f"Hello, {user_name}!")
# print('Answer "yes" if the number is even, otherwise answer "no".')

# count = 3
# num = random.randint(1, 100)
# def game():
#     if num in range(count):
#         num % 2 == 0
#         # print("Question:  {}".format(num))
#         # user_answer = input("Your answer : ")

# def get_type_of_sentence(sentence):
#     last_char = sentence[-1]

#     if last_char == '?':
#         sentence_type = 'question'
#     else:
#         sentence_type = 'normal'

#     return "Sentence is " + sentence_type

# # print(get_type_of_sentence('Hodor'))
# print(get_type_of_sentence('Hodor?'))

# def print_numbers(numbers):
#     i = 4
#     while numbers < i:
#         print(i)
#         i -= 1
#     print('finished')
# print_numbers(0)



# def join_numbers_from_range(start, finish):
#     i = start
#     result = ''
#     while i <= finish:
#         print(result, str(i))
#         i += 1


# join_numbers_from_range(1, 5)

# def my_substr(strings, lenght):
#     index = 0
#     res_lenght = ''
#     while index < lenght:
#         res_lenght = res_lenght + strings[index]
#         index += 1
#         return res_lenght
# my_substr('hexlet', 6)

# def func_char(text, char):
#     result = 0
#     for current_char in text:
#         if current_char.lower() == char.lower():
#             result += 1
#     return result
# print(func_char('radar!', 'a'))

#  def sum(numbers):
#      result = 0
#      for num in numbers:
#          result += 3
#      return result

#  print(sum("12345")) # 15

# def is_instanse(string):
#    strings = 0
#    strings1 = len(string) -1
#    while strings > 0:
#        if string[strings] == string[strings]:
#            return False
#        strings += 1
#        strings1 -= 1
#    return True
# print(is_instanse('radar'))



# from random import randint


# def is_instans():
#     number1 = int(input())
#     curcl = 3
#     i = randint(0, 30)
#     if i < number1:
#         print('Вы не угадали !')
#         # curcl += 1
#     else:
#         print('Вы угадали !')
#     return number1

# print(is_instans())
# import prompt 


# from random import randint

# print("Welcome to the Brain Games!")
# user_name = input("May I have your name? ")
# print(f"Hello, {user_name}!")
# print('Answer "yes" if the number is even, otherwise answer "no".')
# curcle = 0
# winscore = 3
# congrats = print('Congratulations, {name}!')
# def is_even_game(even):
#     while curcle < 4:
#         random_number = randint(1, 100)
#         answer = input()
#         if random_number % 2 == 0 and answer == "Yes":
#             print("Correct {} !".format (answer))
#             curcle += 3
#             break
#         elif random_number % 2 != 0 and answer != "No":
#             print("No Correct {} !".format (answer))
#             break
#         else:
#             print("Game Over !")
#         break


# def transcate(text, lenght):
#     result = f"{text [:lenght]}..."
#     return result 
# print(transcate("Hexlet"))


# from random import randint
import random


# def is_calc_game():
#     curcle = 0
#     print("Welcome to the Brain Games!")
#     user_name = input("May I have your name? ")
#     print(f"Hello, {user_name.capitalize()}!")
#     print('What is the result of the expression?')
    
#     for i in range(0, 3):
        
#         random_number = randint(0, 20)
#         random_number1 = randint(10, 30)
#         value = ['+','-','*']
#         value_answer = random.choice(value)
#         print("Questions : {}".format(random_number),(value_answer),(random_number1))
#         answer = int(input())

#         if  value_answer == '+' and random_number + random_number1:
#             print(f"Your answer : {answer}!")
#             print("Correct !". format())
#             curcle += 1

#         elif value_answer == '-' and random_number - random_number1:
#             print(f"Your answer : {answer}!")
#             print("Correct !". format(answer))
#             curcle += 1

#         elif value_answer == '*' and random_number - random_number1:
#             print(f"Your answer : {answer}!")
#             print("Correct !". format(answer))
#             curcle += 1

#         else:
#             right_answer = f"{random_number} {value_answer} {random_number1}"
#             print(f"'{answer}' is wrong answer ;(. Correct answer was '{eval(right_answer)}'.Let\'s try again, {user_name.capitalize()} !")
#             break

#     if curcle == 3:
#         print(f"Congratulations, {user_name.capitalize()}!")

# is_calc_game()

#
# from random import randint
# import random
#
#
# def is_calc_game():
#     curcle = 0
#     print("Welcome to the Brain Games!")
#     user_name = input("May I have your name? ")
#     print(f"Hello, {user_name.capitalize()}!")
#     print('What is the result of the expression?')
#
#     for i in range(0, 3):
#         random_number1 = randint(0, 20)
#         random_number2 = randint(1, 18)
#         value = ['+', '-', '*']
#         value_answer = random.choice(value)
#         operation = f"{random_number1} {value_answer} {random_number2}"
#         print("Questions : {}".format(operation))
#         answer = int(input())
#
#         if value_answer == '+' and answer == eval(operation):
#             print(f"Your answer : {answer}!")
#             print("Correct !".format())
#             curcle += 1
#
#         elif value_answer == '-' and answer == eval(operation):
#             print(f"Your answer : {answer}!")
#             print("Correct !".format())
#             curcle += 1
#
#         elif value_answer == '*' and answer == eval(operation):
#             print(f"Your answer : {answer}!")
#             print("Correct !".format())
#             curcle += 1
#
#         else:
#             print(
#                 f"'{answer}' is wrong answer ;(. Correct answer was '{eval(operation)}'.Let\'s try again, {user_name.capitalize()} !")
#             break
#
#     if curcle == 3:
#         print(f"Congratulations, {user_name.capitalize()}!")
#
#
# is_calc_game()
