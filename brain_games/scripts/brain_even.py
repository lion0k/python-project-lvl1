#!/usr/bin/env python

"""Game Brain Even."""

from brain_games.engine import start_play
from brain_games.games import brain_even_module


def main():
    """Do main loop start the game."""
    start_play(brain_even_module)


if __name__ == '__main__':
    main()
