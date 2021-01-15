"""Game brain even logic."""

from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
GAME_RANGE = (0, 30)


def is_even(number: int) -> bool:
    """
    Check if number is even.

    Args:
        number: number to check

    Returns:
        bool
    """
    return number % 2 == 0


def get_question_and_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: contains question and correct answer
    """
    question = randint(*GAME_RANGE)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
