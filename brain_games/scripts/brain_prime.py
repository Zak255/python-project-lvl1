#!/usr/bin/env python
from brain_games.games import prime
from brain_games.games.prime import *

welcome_prime(is_prime(2),make_question(),logic_user())

def main():
    prime(welcome_prime)

if __name__ == "__main__":
    main()
