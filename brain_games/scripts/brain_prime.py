#!/usr/bin/env python3
from brain_games.games import prime
from brain_games.games.prime import *

function_games = welcome_prime(),is_prime(2),make_question(),logic_user()

def main():
    prime(function_games)

if __name__ == "__main__":
    main()
