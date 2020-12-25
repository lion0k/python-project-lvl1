"""Game engine and additional functions."""

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


def start_play(game):
    """
    Start game.

    Args:
        game: game module
    """
    user_name = welcome_user()
    print_description(game.DESCRIPTION)

    for step in range(1, NUMBER_STEPS_TO_PLAY + 1):
        question, correct_answer = game.make_question_and_get_correct_answer()
        user_answer = set_question(question)
        if user_answer != correct_answer:
            print_wrong_answer(
                user_name,
                user_answer,
                correct_answer,
            )
            break
        print_success_answer()

        if step == NUMBER_STEPS_TO_PLAY:
            print_end_game(user_name)
