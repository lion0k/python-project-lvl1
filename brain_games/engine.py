"""Game engine and additional functions."""

import prompt

from brain_games.cli import welcome_user

NUMBER_STEPS_TO_PLAY = 3
WRONG_ANSWER = (
    "'{user_answer}' is wrong answer ;(."
    +
    " Correct answer was '{correct_answer}'."
)
TRY_AGAIN = "Let's try again, {user_name}!"
END_GAME = 'Congratulations {user_name}!'


def inform_user(template: str, **kwargs):
    """
    Set output information.

    Args:
        template: template for print
        kwargs: possible args
    """
    print(template.format(**kwargs))


def ask_question(question: str) -> str:
    """
    Ask a question to the user.

    Args:
        question: game question

    Returns:
        str: the user's answer to the question
    """
    inform_user('Question: {question}', question=question)
    return prompt.string('Your answer: ')


def play(game):
    """
    Start game.

    Args:
        game: game module
    """
    user_name = welcome_user()
    inform_user(game.DESCRIPTION)

    for step in range(1, NUMBER_STEPS_TO_PLAY + 1):
        question, correct_answer = game.get_question_and_correct_answer()
        user_answer = ask_question(question)
        if user_answer != correct_answer:
            inform_user(
                WRONG_ANSWER,
                user_answer=user_answer,
                correct_answer=correct_answer,
            )
            inform_user(TRY_AGAIN, user_name=user_name)
            break
        inform_user('Correct!')

        if step == NUMBER_STEPS_TO_PLAY:
            inform_user(END_GAME, user_name=user_name)
