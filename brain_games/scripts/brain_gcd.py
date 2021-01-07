#!/usr/bin/env python

"""Game Great Common Divider."""

from brain_games.engine import play
from brain_games.games import gcd


def main():
    """Do main loop start the game."""
    play(gcd)


if __name__ == '__main__':
    main()
