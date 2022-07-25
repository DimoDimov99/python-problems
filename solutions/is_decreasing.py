from utils.test_program_output import test_output


def is_decreasing(number_set):
    for number in range(len(number_set) - 1):
        if number_set[number] > number_set[number + 1]:
            return True
        return False


test_data = [
    (True, [5, 4, 3, 2 ,1]),
    (False, [1, 2, 3]),
    (True, [100, 50, 20]),
    (False, [1, 1, 1, 1])
]


if __name__ == "__main__":
    test_output(test_data, is_decreasing)
