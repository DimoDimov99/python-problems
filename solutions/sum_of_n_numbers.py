from utils.test_program_output import test_output


def gauss_n_sum(_input):
    return (_input * (_input + 1)) // 2


test_data = [(10, 55), (5, 15), (100, 5050)]

if __name__ == "__main__":
    test_output(test_data, gauss_n_sum, True)
