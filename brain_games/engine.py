"""Game engine and additional functions."""

from collections import namedtuple
from random import randint

from brain_games.cli import (
    print_description,
    print_end_game,
    print_success_answer,
    print_wrong_answer,
    set_question,
    welcome_user,
)

COUNT_PLAY_TRY = 3


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


def start_play(description: str, iter_func_game):
    """
    Start game iterations.

    Args:
        description: game description
        iter_func_game: function game
    """
    user_name = welcome_user()
    print_description(description)
    count = COUNT_PLAY_TRY

    while count:
        iter_game = iter_func_game()
        user_answer = set_question(iter_game.question)
        if user_answer != iter_game.answer:
            print_wrong_answer(user_name, user_answer, iter_game.answer)
            break
        print_success_answer()
        count -= 1

    if not count:
        print_end_game(user_name)
