"""Game brain gcd logic."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
GAME_RANGE = (0, 30)


def gcd(op1: int, op2: int) -> int:
    """
    Found great common divisor.

    Args:
        op1: operand 1
        op2: operand 2

    Returns:
        int
    """
    if (op1 == 0) or (op2 == 0):
        return max(op1, op2)
    op_min = min(op1, op2)
    return gcd(max(op1, op2) % op_min, op_min)


def get_question_and_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: contains question and correct answer
    """
    operand1, operand2 = [randint(*GAME_RANGE) for _ in range(2)]
    question = '{v1} {v2}'.format(
        v1=operand1,
        v2=operand2,
    )
    answer = gcd(operand1, operand2)
    return question, str(answer)
