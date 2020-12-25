#!/usr/bin/env python

"""Game Great Common Divider."""

from brain_games.engine import start_play
from brain_games.games import brain_gcd_module


def main():
    """Do main loop start the game."""
    start_play(brain_gcd_module)


if __name__ == '__main__':
    main()
