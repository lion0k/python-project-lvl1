#!/usr/bin/env python

"""Game Brain Prime."""

from brain_games.engine import start_play
from brain_games.games.brain_prime_module import iter_brain_prime

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    """Do main loop start the game."""
    start_play(DESCRIPTION, iter_brain_prime)


if __name__ == '__main__':
    main()
