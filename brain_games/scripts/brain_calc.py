#!/usr/bin/env python

"""Game Brain Calculation."""

from brain_games.engine import play
from brain_games.games import calc


def main():
    """Do main loop start the game."""
    play(calc)


if __name__ == '__main__':
    main()
