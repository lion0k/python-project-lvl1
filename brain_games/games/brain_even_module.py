"""Game brain even logic."""

from brain_games.engine import get_random_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_odd(number: int) -> str:
    """
    Parity check.

    Args:
        number: number to check

    Returns:
        str: 'yes' or 'no'
    """
    return 'yes' if number % 2 == 0 else 'no'


def make_question_and_get_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: namedtuple contains question and correct answer
    """
    number = get_random_number()
    return number, is_odd(number)
