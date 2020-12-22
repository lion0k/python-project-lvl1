#!/usr/bin/env python

"""Game Great Common Divider."""

from brain_games.engine import start_play
from brain_games.games.brain_gcd_module import iter_brain_gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def main():
    """Do main loop start the game."""
    start_play(DESCRIPTION, iter_brain_gcd)


if __name__ == '__main__':
    main()
