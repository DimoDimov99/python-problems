from utils.test_program_output import test_output


def is_decreasing(number_set):
    for number in range(len(number_set) - 1):
        if number_set[number] > number_set[number + 1]:
            return True
        return False


test_data = [
    ([5, 4, 3, 2, 1], True),
    ([1, 2, 3], False),
    ([100, 50, 20], True),
    ([1, 1, 1, 1], False)
]


if __name__ == "__main__":
    test_output(test_data, is_decreasing, True)
