"""Game arithmetic progression logic."""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'
GAME_RANGE = (0, 9)
STEP_PROGRESSION_RANGE = (0, 10)
START_PROGRESSION_RANGE = (0, 50)


def get_random_progression() -> list:
    """
    Get random progression list.

    Returns:
         list
    """
    start_number = randint(*START_PROGRESSION_RANGE)
    step = randint(*STEP_PROGRESSION_RANGE)
    stop_number = step * 10 + start_number
    return [str(number) for number in range(start_number, stop_number, step)]


def get_question_and_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: contains question and correct answer
    """
    progression = get_random_progression()
    random_value = randint(*GAME_RANGE)
    answer = progression[random_value]
    progression[random_value] = '..'
    question = ' '.join(progression)
    return question, answer
