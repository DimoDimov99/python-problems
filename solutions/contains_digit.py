from utils.test_program_output import test_output


def contains_digit(number, digit):
    str_number = str(number)

    for _digit in str_number:
        if int(_digit) == digit:
            return True

    return False


test_data = [
    ((123, 4), False),
    ((42, 4), True),
    ((1000, 0), True),
    ((12346789, 5), False)
]


if __name__ == "__main__":
    test_output(test_data, contains_digit, True, 2)
