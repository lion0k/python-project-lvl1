"""Game brain calc logic."""

from operator import add, mul, sub
from random import randint

DESCRIPTION = 'What is the result of the expression?'
GAME_RANGE = (0, 30)
OPERATIONS = {'+': add, '-': sub, '*': mul}


def get_question_and_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: contains question and correct answer
    """
    operand1, operand2 = [randint(*GAME_RANGE) for _ in range(2)]
    current_operation = list(OPERATIONS)[randint(0, len(OPERATIONS) - 1)]
    answer = OPERATIONS[current_operation](operand1, operand2)
    question = '{value1} {operation} {value2}'.format(
        value1=operand1,
        operation=current_operation,
        value2=operand2,
    )
    return question, str(answer)
