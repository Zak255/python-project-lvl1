#!/usr/bin/env python
from brain_games.games.prime import welcome_prime
from brain_games.games.prime import is_prime
from brain_games.games.prime import make_question
from brain_games.games.prime import logic_user



def main():
    welcome_prime()
    is_prime(2)
    make_question()
    logic_user()
if __name__ == "__main__":
    main()
