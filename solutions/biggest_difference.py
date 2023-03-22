from utils.test_program_output import test_output


def get_min_elem(arr):
    _min = arr[0]

    for elem in arr:
        if elem < _min:
            _min = elem
    return _min


def get_max_elem(arr):
    _max = arr[0]

    for elem in arr:
        if elem > _max:
            _max = elem
    return _max


def biggest_difference(arr):
    min_elem = get_min_elem(arr)
    max_elem = get_max_elem(arr)

    return min_elem - max_elem


test_data = [
    ([1, 2], -1),
    ([1, 2, 3, 4, 5], -4),
    ([-10, -9, -1], -9),
]


if __name__ == "__main__":
    test_output(test_data, biggest_difference, True)
