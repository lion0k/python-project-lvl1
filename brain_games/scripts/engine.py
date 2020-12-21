"""Game engine and additional functions."""

from collections import namedtuple
from random import randint


def get_random_number(min_number=1, max_number=100) -> int:
    """
    Get an random number from range.

    Args:
        min_number: minimum number, default = 1
        max_number: maximum number, default = 100

    Returns:
        int
    """
    return randint(min_number, max_number)


def is_odd(number: int) -> str:
    """
    Parity check.

    Args:
        number: number to check

    Returns:
        str: 'yes' or 'no'
    """
    return 'yes' if number % 2 == 0 else 'no'


def is_correct_input_number(input_str: str) -> namedtuple:
    """
    Check the input string for a number.

    Args:
        input_str: string to check

    Returns:
        tuple:
    """
    number = namedtuple('InputNumber', 'success result')
    try:
        return number(success=True, result=int(input_str))
    except ValueError:
        return number(success=False, result=-1)
