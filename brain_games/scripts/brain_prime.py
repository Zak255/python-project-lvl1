#!/usr/bin/env python
from brain_games.games import prime
from brain_games.games.prime import welcome_prime
from brain_games.games.prime import is_prime
from brain_games.games.prime import make_question
from brain_games.games.prime import logic_user

function_games = welcome_prime(),is_prime(2),make_question(),logic_user()

def main():
    prime(function_games)


if __name__ == "__main__":
    main()
