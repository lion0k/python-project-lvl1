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
