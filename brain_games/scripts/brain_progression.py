#!/usr/bin/env python

"""Game arithmetic progression."""

from brain_games.engine import start_play
from brain_games.games import brain_progression_module


def main():
    """Do main loop start the game."""
    start_play(brain_progression_module)


if __name__ == '__main__':
    main()
