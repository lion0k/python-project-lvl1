"""Command line interface."""

import prompt


def welcome_user():
    """Get input user name and greet the user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
