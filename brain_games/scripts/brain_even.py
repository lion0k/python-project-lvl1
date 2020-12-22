#!/usr/bin/env python

"""Game Brain Even."""

from brain_games.engine import start_play
from brain_games.games.brain_even_module import iter_brain_even

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    """Do main loop start the game."""
    start_play(DESCRIPTION, iter_brain_even)


if __name__ == '__main__':
    main()
