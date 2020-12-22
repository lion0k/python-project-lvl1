"""Game brain calc logic."""

from collections import namedtuple
from operator import add, mul, sub

from brain_games.engine import get_random_number, set_question_and_answer

OPERATIONS = ('+', '-', '*')


def get_random_operation() -> namedtuple:
    """
    Get an random operation.

    Returns:
        namedtuple: contains current operation and function
    """
    operations_func = {'+': add, '-': sub, '*': mul}
    op_random = namedtuple('OperationRandom', 'operation operation_func')
    current_operation = OPERATIONS[get_random_number(0, 2)]
    return op_random(
        operation=current_operation,
        operation_func=operations_func[current_operation],
    )


def iter_brain_calc() -> tuple:
    """
    Run iteration game function.

    Returns:
        tuple: namedtuple contains question and correct answer
    """
    operand1, operand2 = [get_random_number() for _ in range(2)]
    operation = get_random_operation()
    question = '{v1} {op} {v2}'.format(
        v1=operand1,
        op=operation.operation,
        v2=operand2,
    )
    answer = operation.operation_func(operand1, operand2)
    return set_question_and_answer(question, str(answer))
