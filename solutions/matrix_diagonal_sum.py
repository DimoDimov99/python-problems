from utils.test_program_output import test_output


def solve(_input):
    result = 0
    for i in range(len(_input)):
        for j in range(len(_input[0])):
            if i == j:
                result += _input[i][j]
    return result


test_data = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15),
    ([[1, 2, 3], [4, 5, 6]], 6),
    ([[]], 0),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 18),
]

if __name__ == "__main__":
    test_output(test_data, solve, True)
