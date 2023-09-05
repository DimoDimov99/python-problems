from utils.test_program_output import test_output


def transpose_matrix(matrix):
    result = []
    matrix_len = len(matrix)
    matrix_elem_len = len(matrix[0])

    for i in range(matrix_elem_len):
        tmp_matrix_set = []
        for j in range(matrix_len):
            tmp_matrix_set.append(matrix[j][i])
        result.append(tmp_matrix_set)
    return result


test_data = [
    ([[2, 4, -1], [-10, 5, 11], [18, -7, 6]], [[2, -10, 18], [4, 5, -7], [-1, 11, 6]]),
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
]
if __name__ == "__main__":
    test_output(test_data, transpose_matrix, True)
