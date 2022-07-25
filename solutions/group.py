from utils.test_program_output import test_output


def group(items):
    result = []
    items_len = len(items)
    index = 0

    while index < items_len:
        current_group = [items[index]]
        next_index = index + 1

        while next_index < items_len and items[next_index] == items[index]:
            current_group.append(items[next_index])
            next_index += 1

        result.append(current_group)
        index = next_index

    return result


test_data = [
    ([[1, 1 ,1], [2], [3], [1, 1]], [1, 1, 1, 2, 3, 1, 1]),
    ([[1], [2], [1], [2], [3, 3]], [1, 2, 1, 2,3, 3]),
    ([], []),
    ([[1]], [1]),
    ([[1, 1, 1, 1]], [1, 1, 1, 1])
]


if __name__ == "__main__":
    test_output(test_data, group, True)
