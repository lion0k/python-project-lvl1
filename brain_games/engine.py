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

NUMBER_STEPS_TO_PLAY = 3


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
    qa = namedtuple('QA', 'question answer')
    return qa(question=question, answer=answer)


def start_play(game):
    """
    Start game.

    Args:
        game: game module
    """
    user_name = welcome_user()
    print_description(game.DESCRIPTION)

    for step in range(1, NUMBER_STEPS_TO_PLAY + 1):
        question_and_answer = game.get_question_and_correct_answer()
        user_answer = set_question(question_and_answer.question)
        if user_answer != question_and_answer.answer:
            print_wrong_answer(
                user_name,
                user_answer,
                question_and_answer.answer,
            )
            break
        print_success_answer()

        if step == NUMBER_STEPS_TO_PLAY:
            print_end_game(user_name)
