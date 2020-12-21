"""Command line interface."""

import prompt


def welcome_user() -> str:
    """
    Get input user name and greet the user.

    Returns:
        str: user's name
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=user_name))
    return user_name


def print_success_answer():
    """Print success answer."""
    print('Correct!')


def print_end_game(user_name: str):
    """
    Print end game.

    Args:
        user_name: user's name
    """
    print('Congratulations {name}!'.format(name=user_name))


def set_question(question: str) -> str:
    """
    Ask a question to the user.

    Args:
        question: question to user

    Returns:
        str
    """
    return prompt.string('Question: {question}'.format(question=question))
