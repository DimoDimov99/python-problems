from utils.test_program_output import test_output
from enum import Enum


class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3


def increasing_or_decreasing(sequance):
    sequance_len = len(sequance)

    if sequance_len <= 1:
        return Monotonicity.NONE

    is_increasing = True
    is_decreasing = True

    for number in range(sequance_len - 1):
        current_number = sequance[number]
        next_number = sequance[number + 1]

        is_increasing = is_increasing and current_number < next_number
        is_decreasing = is_decreasing and current_number > next_number

    if is_increasing:
        return Monotonicity.INCREASING

    if is_decreasing:
        return Monotonicity.DECREASING

    return Monotonicity.NONE


test_data = [
    ([1,  2, 3, 4, 5], Monotonicity.INCREASING),
    ([5,  6, -10], Monotonicity.NONE),
    ([1,  1, 1, 1], Monotonicity.NONE),
    ([9,  8, 7, 6], Monotonicity.DECREASING),
    ([],  Monotonicity.NONE),
    ([1],  Monotonicity.NONE),
    ([1,  100], Monotonicity.INCREASING),
    ([1,  100, 100], Monotonicity.NONE),
    ([100,  1], Monotonicity.DECREASING),
    ([100,  1, 1], Monotonicity.NONE),
    ([100,  1, 2], Monotonicity.NONE),
]


if __name__ == "__main__":
    test_output(test_data, increasing_or_decreasing, True)
