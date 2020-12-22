#!/usr/bin/env python

"""Game Brain Calculation."""

from brain_games.engine import (
    get_random_number,
    get_random_operation,
    set_question_and_answer,
    start_play,
)

DESCRIPTION = 'What is the result of the expression?'


def _iter_brain_calc() -> tuple:
    """
    Run iteration game function.

    Returns:
        tuple: namedtuple contains question and correct answer
    """
    operand1, operand2 = [get_random_number() for _ in range(2)]
    operation = get_random_operation()
    question = '{v1} {op} {v2}'.format(
        v1=operand1,
        op=operation.operation,
        v2=operand2,
    )
    answer = operation.operation_func(operand1, operand2)
    return set_question_and_answer(question, str(answer))


def main():
    """Do main loop start the game."""
    start_play(DESCRIPTION, _iter_brain_calc)


if __name__ == '__main__':
    main()
