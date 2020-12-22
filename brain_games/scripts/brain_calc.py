#!/usr/bin/env python

"""Game Brain Calculation."""

from brain_games.engine import start_play
from brain_games.games.brain_calc_module import iter_brain_calc

DESCRIPTION = 'What is the result of the expression?'


def main():
    """Do main loop start the game."""
    start_play(DESCRIPTION, iter_brain_calc)


if __name__ == '__main__':
    main()
