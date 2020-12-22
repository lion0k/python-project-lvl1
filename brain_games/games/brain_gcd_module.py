"""Game brain gcd logic."""

from brain_games.engine import get_random_number, set_question_and_answer


def gcd(op1: int, op2: int) -> int:
    """
    Found great common divider.

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


def iter_brain_gcd() -> tuple:
    """
    Run iteration game function.

    Returns:
        tuple: namedtuple contains question and correct answer
    """
    operand1, operand2 = [get_random_number() for _ in range(2)]
    question = '{v1} {v2}'.format(
        v1=operand1,
        v2=operand2,
    )
    answer = gcd(operand1, operand2)
    return set_question_and_answer(question, str(answer))
