"""Game brain gcd logic."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
GAME_RANGE = (0, 30)


def gcd(operand1: int, operand2: int) -> int:
    """
    Find great common divisor.

    Args:
        operand1: operand 1
        operand2: operand 2

    Returns:
        int
    """
    if (operand1 == 0) or (operand2 == 0):
        return max(operand1, operand2)
    operand_min = min(operand1, operand2)
    return gcd(max(operand1, operand2) % operand_min, operand_min)


def get_question_and_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: contains question and correct answer
    """
    operand1, operand2 = [randint(*GAME_RANGE) for _ in range(2)]
    question = '{value1} {value2}'.format(
        value1=operand1,
        value2=operand2,
    )
    answer = gcd(operand1, operand2)
    return question, str(answer)
