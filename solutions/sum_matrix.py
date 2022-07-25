from utils.test_program_output import test_output


def sum_matrix(m):
    _sum = 0
    for i in m:
        for j in i:
            _sum += j

    return _sum


test_data = [
    (45, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    (0, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    (55, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
]

if __name__ == "__main__":
    test_output(test_data, sum_matrix)

