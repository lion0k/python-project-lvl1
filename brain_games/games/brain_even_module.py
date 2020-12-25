"""Game brain even logic."""

from brain_games.engine import get_random_number, set_question_and_answer

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


def get_question_and_correct_answer() -> tuple:
    """
    Get a question and prepare a correct answer.

    Returns:
        tuple: namedtuple contains question and correct answer
    """
    number = get_random_number()
    return set_question_and_answer(number, is_odd(number))
