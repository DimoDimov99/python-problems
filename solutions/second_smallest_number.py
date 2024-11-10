from utils.test_program_output import test_output


def second_smallest_number(_input):
    # this is done in order for the display from test_program_output.py to be correct (should be deep copy)
    _input_copy = _input[::]
    _min = _input_copy[0]
    _min_index = 0
    counter = 0
    times_iterate = 0
    l = len(_input_copy)
    while counter < l:
        if _input_copy[counter] < _min:
            _min = _input_copy[counter]
            _min_index = counter
        counter += 1
        if counter == l and times_iterate < 1:
            _input_copy.pop(_min_index)
            l -= 1
            counter = 0
            _min = _input_copy[counter]
            times_iterate += 1
    return _min


test_data = [
    ([1, 2, 3, 5, 10, -6], 1),
    ([105, -6, 0], 0),
    ([10, 11], 11),
    ([2, 4, 6, 8, 10], 4),
    ([-6, -10, -8, 5, 40, 30], -8),
]

if __name__ == "__main__":
    test_output(test_data, second_smallest_number, True)
