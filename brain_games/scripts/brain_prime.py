#!/usr/bin/env python
from brain_games.games import prime
from brain_games.games.prime import *


def main():
    prime()
def welcome_prime():
    prime(main)
def is_prime():
    welcome_prime()
def make_question():
    is_prime(2)
def logic_user():
    make_question()

if __name__ == "__main__":
    main()
