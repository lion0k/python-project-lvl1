"""Game brain calc logic."""

from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'
GAME_RANGE = (0, 30)
OPERATIONS = '+-*'


def calculate(operand1: str, operand2: str, operation: str) -> int:
    """
    Calculate correct answer.

    Args:
        operand1: operand 1
        operand2: operand 2
        operation: operation on operands

    Returns:
        int
    """
    if operation == '+':
        return add(operand1, operand2)
    elif operation == '-':
        return sub(operand1, operand2)
    elif operation == '*':
        return mul(operand1, operand2)


def get_question_and_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: contains question and correct answer
    """
    operand1 = randint(*GAME_RANGE)
    operand2 = randint(*GAME_RANGE)
    current_operation = choice(OPERATIONS)
    answer = str(calculate(operand1, operand2, current_operation))
    question = '{value1} {operation} {value2}'.format(
        value1=operand1,
        operation=current_operation,
        value2=operand2,
    )
    return question, answer
