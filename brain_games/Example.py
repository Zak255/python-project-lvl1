# dictionary = {
#     "foo": "bar",
#     "baz": 42,
#     "items": {
#         1: "apple",
#         2: "orange",
#         100500: "lemon"
#     },
# }
# print(dictionary.get("BANG", "no such key"))


# for k in {"a": 1, "b": 2}:
#     print(k)

# print(list({"a": 1, "b": 2}.keys()))

# print(list({"a": 1, "b": 2}.values()))

# for k, v in {"a": 1, "b": 2}.items():
#     print(k, "=", v)

# '''В этой практике вам нужно реализовать две функции:
# функцию make_user(), которая должна принимать два параметра — имя пользователя и возраст (число).
# Вернуть функция должна словарь с ключами 'name' и 'age',
# по которым должны быть сохранены соответствующие значения.
# функцию format_user(), которая, будучи применена к результату вызова make_user()
# (помним — это словарь), должна вернуть строку вида 'Phil, 25'.'''

# def make_user(name, age):
#     return {'name': name, 'age': age}
# print(make_user('hexlet', 35))


# def format_user(user):
#     return f"{user['name']}, {user['age']}"
# print(format_user(make_user('hexlet', 35)))

# d = {} # пустой словарь
# d["a"] = 100
# print(d)

# d["b"] = 200
# d["a"] = 0
# print(d)

# # Метод POP удаление элементов
# # из словаря
# d = {'a': 1, 'b': 2}
# d.pop('a')
# print(d)
# d.pop('BANG')
# print(d)

# d = {'a': 1, 'b': 2}
# print(d.pop('BANG', None))
# print(d.pop('BANG', 42))
# print(d)
# d = {'a': 1}
# print(d.popitem())
# # d.popitem()
# # print(d)

# cart = {'apples': 2, 'oranges': 1}
# addon = {'oranges': 5, 'lemons': 3}
# cart.update(addon)
# print(cart)

# d = {'a': 1, 'b': [42]}
# c = d.copy()
# c.update({'a': 10, '1k': 1024})
# print(c)
# c['b'].append(None)
# print(c)
# c.pop('a')
# print(c)
# print(d)
# # МЕТОД Clear() удаляет все элементы текущего словаря
# #
# d = {'a': 1}
# d.clear()
# print(d)

# Цель упражнения — функция count_all().
# Эта функция должна принимать на вход iterable источник и возвращать словарь,
#  ключами которого являются элементы источника,
# а значения отражают количество повторов элемента в коллекции-источнике.
# Вот пара примеров, демонстрирующих то, как функция должна работать:

# def count_all(items):
#     couter = {}
#     for i in items:
#         couter[i] = couter.get(i, 0) + 1
#     return couter
# print(count_all('*' * 20))
# from collections import defaultdict
# d = defaultdict(int)
# d['a'] += 5
# d['b'] = d['c'] + 10
# print(d)
from brain_games.cli import question_and_correct_answer(), correct_answer_massage
import prompt


def run_game(game_name):
    name = question_and_correct_answer()()
    print(game_name.DESCRIPTION)
    curcle = 0
    for _ in range(0, 3):
        question, answer = game_name.question_and_correct_answer()
        print("Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if not (user_answer == answer):
            return correct_answer_massage(user_answer, answer, name)

        print("Correct!")
        curcle += 1
    else:
        print(f"Congratulations, {name}!")


print(run_game(question_and_correct_answer()))
