"""Game brain even logic."""

from brain_games.engine import get_random_number, set_question_and_answer


def is_odd(number: int) -> str:
    """
    Parity check.

    Args:
        number: number to check

    Returns:
        str: 'yes' or 'no'
    """
    return 'yes' if number % 2 == 0 else 'no'


def iter_brain_even() -> tuple:
    """
    Run iteration game function.

    Returns:
        tuple: namedtuple contains question and correct answer
    """
    number = get_random_number()
    return set_question_and_answer(number, is_odd(number))
