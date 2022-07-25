from utils.test_program_output import test_output


def max_consecutive(items):
    max_times = 0
    index = 0

    while index < len(items):
        next_max_times = 1
        next_index = index + 1

        while next_index < len(items) and items[next_index] == items[index]:
            next_max_times += 1
            next_index += 1

        if next_max_times > max_times:
            max_times = next_max_times

        index = next_index

    return max_times


test_data = [
    (4, [1, 2, 3, 3, 3, 3, 4, 3, 3]),
    (3, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]),
    (1, [1]),
    (0, []),
    (6, [6, 6, 6, 6, 1, 6, 6, 6, 6, 6, 6, 5])
]


if __name__ == "__main__":
    test_output(test_data, max_consecutive, True)
