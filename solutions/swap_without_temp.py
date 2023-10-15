from utils.test_program_output import test_output


def swap_without_temp(elems):
    elems[0] = elems[0] + elems[1]
    elems[1] = elems[0] - elems[1]
    elems[0] = elems[0] - elems[1]
    return elems


test_data = [
    ([4, 5], [5, 4]),
    ([6, 5], [5, 6]),
    ([-5, 60], [60, -5]),
]

if __name__ == "__main__":
    test_output(test_data, swap_without_temp, True)
