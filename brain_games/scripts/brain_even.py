#!/usr/bin/env python

"""Game Brain Even."""

from collections import namedtuple

from brain_games.engine import get_random_number, is_odd, start_play

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def _iter_brain_even() -> namedtuple:
    """
    Run iteration game function.

    Returns:
        namedtuple: contains question and correct answer
    """
    number = get_random_number()
    game_iter = namedtuple('GameIter', 'question, answer')
    return game_iter(question=number, answer=is_odd(number))


def main():
    """Do main loop start the game."""
    start_play(DESCRIPTION, _iter_brain_even)


if __name__ == '__main__':
    main()
