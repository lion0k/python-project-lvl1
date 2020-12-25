#!/usr/bin/env python

"""Game Brain Prime."""

from brain_games.engine import start_play
from brain_games.games import brain_prime_module


def main():
    """Do main loop start the game."""
    start_play(brain_prime_module)


if __name__ == '__main__':
    main()
