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


def get_random_number(min_num=1, max_num=30) -> int:
    """
    Get an random number from range.

    Args:
        min_num: minimum number, default = 1
        max_num: maximum number, default = 30

    Returns:
        int
    """
    return randint(min_num, max_num)


def set_question_and_answer(question, answer: str) -> namedtuple:
    """
    Check the input string for a number.

    Args:
        question: question to the user
        answer: correct answer

    Returns:
        namedtuple: contains question and correct answer
    """
    game_iter = namedtuple('GameIter', 'question answer')
    return game_iter(question=question, answer=answer)


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
