"""Game engine and additional functions."""

import prompt

NUMBER_STEPS_TO_PLAY = 3
WRONG_ANSWER = (
    "'{user_answer}' is wrong answer ;(."
    +
    " Correct answer was '{correct_answer}'."
)
TRY_AGAIN = "Let's try again, {user_name}!"
END_GAME = 'Congratulations {user_name}!'
WELCOME_THE_GAMES = 'Welcome to the Brain Games!'
ASK_USER_NAME = 'May I have your name? '
GREETING_THE_USER = 'Hello, {name}!'
QUESTION = 'Question: {question}'
USER_ANSWER = 'Your answer: '
CORRECT_ANSWER = 'Correct!'


def inform_user(template: str, **kwargs):
    """
    Set output information.

    Args:
        template: template for print
        kwargs: possible args
    """
    print(template.format(**kwargs))


def ask_question(template: str, input_string: str, **kwargs) -> str:
    """
    Ask a question to the user.

    Args:
        template: game question
        input_string: ask the user for an answer
        kwargs: possible args

    Returns:
        str: the user's answer to the question
    """
    if template:
        inform_user(template, **kwargs)
    return prompt.string(input_string)


def play(game):
    """
    Start game.

    Args:
        game: game module
    """
    inform_user(WELCOME_THE_GAMES)
    user_name = ask_question('', ASK_USER_NAME)
    inform_user(GREETING_THE_USER, name=user_name)

    inform_user(game.DESCRIPTION)

    for step in range(1, NUMBER_STEPS_TO_PLAY + 1):
        question, correct_answer = game.get_question_and_correct_answer()
        user_answer = ask_question(QUESTION, USER_ANSWER, question=question)
        if user_answer != correct_answer:
            inform_user(
                WRONG_ANSWER,
                user_answer=user_answer,
                correct_answer=correct_answer,
            )
            inform_user(TRY_AGAIN, user_name=user_name)
            break
        inform_user(CORRECT_ANSWER)

        if step == NUMBER_STEPS_TO_PLAY:
            inform_user(END_GAME, user_name=user_name)
