"""Game arithmetic progression logic."""

from brain_games.engine import get_random_number, set_question_and_answer

DESCRIPTION = 'What number is missing in the progression?'


def get_random_progression() -> list:
    """
    Get random progression list.

    Returns:
         list
    """
    start_number = get_random_number(max_num=50)
    step = get_random_number(max_num=10)
    stop_number = step * 10 + start_number
    return [str(_) for _ in range(start_number, stop_number, step)]


def get_question_and_correct_answer() -> tuple:
    """
    Get a question and prepare a correct answer.

    Returns:
        tuple: namedtuple contains question and correct answer
    """
    progression = get_random_progression()
    random_value = get_random_number(min_num=0, max_num=9)
    answer = progression[random_value]
    progression[random_value] = '..'
    question = ' '.join(progression)
    return set_question_and_answer(question, answer)
