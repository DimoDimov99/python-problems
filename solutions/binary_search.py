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


# provided _input must be sorted (low to high) and only unique numbers
def binary_search(_input, item):
    _input = set(_input)  # only unique entries for corner cases
    _input = list(_input)  # converted back to list in order to be iterated
    _input = bubble_sort(_input)  # sorting the list for the binary search
    _input_len = len(_input) - 1
    low = 0
    high = _input_len

    while low <= high:
        mid = (high + low) // 2
        if _input[mid] < item:
            low = mid + 1
        elif _input[mid] > item:
            high = mid - 1
        else:
            return mid
    return -1


test_data = [
    (([1, 2, 3, 3], 1), 0),
    (([0, 0, 0], 0), 0),
    (([5, 4, 10], 11), -1),
    (([3, 6, 9], 9), 2),
    (([6], 6), 0),
]

if __name__ == "__main__":
    test_output(test_data, binary_search, True, 2)
