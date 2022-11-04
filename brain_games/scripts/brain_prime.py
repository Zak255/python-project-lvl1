#!/usr/bin/env python3
from brain_games.games import prime
from brain_games.games.prime import *


def main():
    prime.welcome_prime()
    prime.is_prime(2)
    prime.make_question()
    prime.logic_user()


if __name__ == "__main__":
    main()
