#!/usr/bin/env python

"""Game Brain Calculation."""

from brain_games.engine import play
from brain_games.games import brain_calc_module


def main():
    """Do main loop start the game."""
    play(brain_calc_module)


if __name__ == '__main__':
    main()
