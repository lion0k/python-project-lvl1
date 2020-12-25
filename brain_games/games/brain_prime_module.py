"""Game brain prime logic."""

from brain_games.engine import get_random_number, set_question_and_answer

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> str:
    """
    Check if the number is prime. Used sieve of Eratosthenes.

    Args:
        number: number to check

    Returns:
        str: 'yes' or 'no'
    """
    arr = [True for _ in range(number + 1)]
    for index in range(2, number + 1):
        if arr[index]:
            for _ in range(index ** 2, number + 1, index):
                arr[_] = False

    return 'yes' if arr[number] else 'no'


def get_question_and_correct_answer() -> tuple:
    """
    Get a question and prepare a correct answer.

    Returns:
        tuple: namedtuple contains question and correct answer
    """
    number = get_random_number(min_num=2, max_num=100)
    return set_question_and_answer(number, is_prime(number))
