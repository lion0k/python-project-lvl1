#!/usr/bin/env python

"""Game Brain Even."""

from brain_games.engine import (
    get_random_number,
    is_odd,
    set_question_and_answer,
    start_play,
)

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def _iter_brain_even() -> tuple:
    """
    Run iteration game function.

    Returns:
        tuple: namedtuple contains question and correct answer
    """
    number = get_random_number()
    return set_question_and_answer(number, is_odd(number))


def main():
    """Do main loop start the game."""
    start_play(DESCRIPTION, _iter_brain_even)


if __name__ == '__main__':
    main()
