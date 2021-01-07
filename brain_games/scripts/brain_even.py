#!/usr/bin/env python

"""Game Brain Even."""

from brain_games.engine import play
from brain_games.games import even


def main():
    """Do main loop start the game."""
    play(even)


if __name__ == '__main__':
    main()
