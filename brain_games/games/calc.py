"""Game brain calc logic."""

from operator import add, mul, sub
from random import randint

DESCRIPTION = 'What is the result of the expression?'
GAME_RANGE = (0, 30)
RANGE_OPERATIONS = (0, 2)
OPERATIONS = ('+', '-', '*')


def get_random_operation(op1: int, op2: int) -> tuple:
    """
    Get an random operation.

    Args:
        op1: operand 1
        op2: operand 2

    Returns:
        tuple: contains current operation and function
    """
    operations_func = {'+': add, '-': sub, '*': mul}
    current_operation = OPERATIONS[randint(*RANGE_OPERATIONS)]
    return (
        current_operation,
        operations_func[current_operation](op1, op2),
    )


def get_question_and_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: contains question and correct answer
    """
    operand1, operand2 = [randint(*GAME_RANGE) for _ in range(2)]
    current_operation, answer = get_random_operation(operand1, operand2)
    question = '{v1} {op} {v2}'.format(
        v1=operand1,
        op=current_operation,
        v2=operand2,
    )
    return question, str(answer)
