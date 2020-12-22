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


def print_wrong_answer(user_name: str, user_answer, correct_answer):
    """
    Print wrong answer.

    Args:
        user_name: user's name
        user_answer: user's answer
        correct_answer: correct answer
    """
    answer = "'{ua}' is wrong answer ;(. Correct answer was '{ca}'."
    print(answer.format(ua=user_answer, ca=correct_answer))
    print("Let's try again, {user_name}!".format(user_name=user_name))


def print_end_game(user_name: str):
    """
    Print end game.

    Args:
        user_name: user's name
    """
    print('Congratulations {name}!'.format(name=user_name))


def print_description(description: str):
    """
    Print description game.

    Args:
        description: description game
    """
    print(description)


def set_question(question: str) -> str:
    """
    Ask a question to the user.

    Args:
        question: question to user

    Returns:
        str
    """
    print('Question: {question}'.format(question=question))
    return prompt.string('Your answer: ')
