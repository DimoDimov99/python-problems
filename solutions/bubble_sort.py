from utils.test_program_output import test_output


def bubble_sort(_input):
    _input_len = len(_input) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, _input_len):
            if _input[i] > _input[i + 1]:
                sorted = False
                _input[i], _input[i + 1] = _input[i + 1], _input[i]
    return _input


test_data = [
    ([3, 2, 1], [1, 2, 3]),
    ([], []),
    ([1, 2], [1, 2]),
    ([1, 5, 6, 6, 10, 15, -1], [-1, 1, 5, 6, 6, 10, 15]),
]

if __name__ == "__main__":
    test_output(test_data, bubble_sort, True)
