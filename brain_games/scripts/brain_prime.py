#!/usr/bin/env python

"""Game Brain Prime."""

from brain_games.engine import play
from brain_games.games import prime


def main():
    """Do main loop start the game."""
    play(prime)


if __name__ == '__main__':
    main()
