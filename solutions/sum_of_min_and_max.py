from utils.test_program_output import test_output


def sum_of_min_and_max(arr):
    arr_len = len(arr)
    if arr_len == 0:
        return 0

    _min = arr[0]
    _max = arr[0]

    for number in range(arr_len):
        if arr[number] < _min:
            _min = arr[number]
        if arr[number] > _max:
            _max = arr[number]

    return _min + _max


test_data = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
    ([-10, 5, 10, 100], 90),
    ([1], 2),
    ([], 0)
]


if __name__ == "__main__":
    test_output(test_data, sum_of_min_and_max, True)
