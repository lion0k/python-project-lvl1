"""Game brain even logic."""

from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
GAME_RANGE = (0, 30)


def is_odd(number: int) -> str:
    """
    Check if number is odd.

    Args:
        number: number to check

    Returns:
        str: 'yes' or 'no'
    """
    return 'yes' if number % 2 == 0 else 'no'


def get_question_and_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: contains question and correct answer
    """
    number = randint(*GAME_RANGE)
    return number, is_odd(number)
