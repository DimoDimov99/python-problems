from utils.test_program_output import test_output


def bubble_sort(arr):
    sorted = False
    arr_len = len(arr) - 1

    while not sorted:
        sorted = True

        for item in range(0, arr_len):
            if arr[item] > arr[item + 1]:
                sorted = False
                arr[item], arr[item + 1] = arr[item + 1], arr[item]

    return arr


def all_possible_numbers_sum(seq, number):
    seq = bubble_sort(seq)
    all_combinations = []
    begin_index = 0
    seq_len = len(seq)
    end_index = seq_len - 1

    while begin_index < end_index:
        if seq[begin_index] + seq[end_index] == number:
            all_combinations.append((seq[begin_index], seq[end_index]))
            begin_index += 1
            end_index -= 1

        elif seq[begin_index] + seq[end_index] > number:
            end_index -= 1

        elif seq[begin_index] + seq[end_index] < number:
            begin_index += 1

    return all_combinations


test_data = [
    (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), [(1, 9), (2, 8), (3, 7), (4, 6)]),
    (
        ([-2, -1, 99, 10, 20, 30, 40, 50, 60, 70, 80, 90, 1, 101, 102], 100),
        [(-2, 102), (-1, 101), (1, 99), (10, 90), (20, 80), (30, 70), (40, 60)],
    ),
    (([], 10), []),
    (([13, 6, -1, 5, 6, 12, 0], 12), [(-1, 13), (0, 12), (6, 6)]),
    (([10, 5, 4, -5, 16, 15, 40], 5), [(-5, 10)]),
]


if __name__ == "__main__":
    test_output(test_data, all_possible_numbers_sum, True, 2)
