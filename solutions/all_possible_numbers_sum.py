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


test_data = [] # todo


if __name__ == "__main__":
    print(all_possible_numbers_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(all_possible_numbers_sum([-2, -1, 99, 10, 20, 30, 40, 50, 60, 70, 80, 90, 1, 101, 102], 100))
    print(all_possible_numbers_sum([], 10))
    print(all_possible_numbers_sum([13, 6, -1, 5, 6, 12, 0], 12))
