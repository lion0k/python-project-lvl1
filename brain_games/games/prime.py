"""Game brain prime logic."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
GAME_RANGE = (2, 100)


def is_prime(number: int) -> str:
    """
    Check if the number is prime. Uses sieve of Eratosthenes.

    Args:
        number: number to check

    Returns:
        str: 'yes' or 'no'
    """
    bool_list = [True for _ in range(number + 1)]
    for index in range(2, number + 1):
        if bool_list[index]:
            for not_prime in range(index ** 2, number + 1, index):
                bool_list[not_prime] = False

    return 'yes' if bool_list[number] else 'no'


def get_question_and_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: contains question and correct answer
    """
    number = randint(*GAME_RANGE)
    return number, is_prime(number)
