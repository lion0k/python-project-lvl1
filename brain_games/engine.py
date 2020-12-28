"""Game engine and additional functions."""

from random import randint

import prompt

from brain_games.cli import welcome_user

NUMBER_STEPS_TO_PLAY = 3
WRONG_ANSWER = "'{ua}' is wrong answer ;(. Correct answer was '{ca}'."
TRY_AGAIN = "Let's try again, {user_name}!"
END_GAME = 'Congratulations {user_name}!'


def set_output(template: str, **kwargs):
    """
    Set output information.

    Args:
        template: template for print
        kwargs: possible args
    """
    print(template.format(**kwargs))


def set_question(question: str) -> str:
    """
    Ask a question to the user.

    Args:
        question: game question

    Returns:
        str: the user's answer to the question
    """
    set_output('Question: {question}', question=question)
    return prompt.string('Your answer: ')


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
    set_output(game.DESCRIPTION)

    for step in range(1, NUMBER_STEPS_TO_PLAY + 1):
        question, correct_answer = game.make_question_and_get_correct_answer()
        user_answer = set_question(question)
        if user_answer != correct_answer:
            set_output(
                WRONG_ANSWER,
                ua=user_answer,
                ca=correct_answer,
            )
            set_output(TRY_AGAIN, user_name=user_name)
            break
        set_output('Correct!')

        if step == NUMBER_STEPS_TO_PLAY:
            set_output(END_GAME, user_name=user_name)
