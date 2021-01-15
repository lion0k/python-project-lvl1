"""Game arithmetic progression logic."""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'
GAME_RANGE = (0, 9)
STEP_PROGRESSION_RANGE = (0, 10)
START_PROGRESSION_RANGE = (0, 50)
NUMBER_OF_VALUES_IN_PROGRESSION = 10


def get_progression(start_number: int, step: int, number_values: int) -> list:
    """
    Get progression list.

    Args:
        start_number: start number progression
        step: step progression
        number_values: number of values in progression

    Returns:
         list
    """
    stop_number = step * number_values + start_number
    return [str(number) for number in range(start_number, stop_number, step)]


def get_question_and_correct_answer() -> tuple:
    """
    Make a question and prepare a correct answer.

    Returns:
        tuple: contains question and correct answer
    """
    progression = get_progression(
        randint(*START_PROGRESSION_RANGE),
        randint(*STEP_PROGRESSION_RANGE),
        NUMBER_OF_VALUES_IN_PROGRESSION,
    )
    random_value = randint(*GAME_RANGE)
    answer = progression[random_value]
    progression[random_value] = '..'
    question = ' '.join(progression)
    return question, answer
