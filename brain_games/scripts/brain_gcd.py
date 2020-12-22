#!/usr/bin/env python

"""Game Great Common Divider."""

from brain_games.engine import (
    gcd,
    get_random_number,
    set_question_and_answer,
    start_play,
)

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def _iter_brain_gcd() -> tuple:
    """
    Run iteration game function.

    Returns:
        tuple: namedtuple contains question and correct answer
    """
    operand1, operand2 = [get_random_number() for _ in range(2)]
    question = '{v1} {v2}'.format(
        v1=operand1,
        v2=operand2,
    )
    answer = gcd(operand1, operand2)
    return set_question_and_answer(question, str(answer))


def main():
    """Do main loop start the game."""
    start_play(DESCRIPTION, _iter_brain_gcd)


if __name__ == '__main__':
    main()
