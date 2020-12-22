#!/usr/bin/env python

"""Game arithmetic progression."""

from brain_games.engine import start_play
from brain_games.games.brain_progression_module import iter_brain_progression

DESCRIPTION = 'What number is missing in the progression?'


def main():
    """Do main loop start the game."""
    start_play(DESCRIPTION, iter_brain_progression)


if __name__ == '__main__':
    main()
