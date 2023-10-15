from utils.test_program_output import test_output


def is_leap_year(_input):
    if _input % 4 == 0:
        if _input % 100 == 0 and _input % 400 == 0:
            return True
        else:
            return False
    return False


test_data = [
    (1600, True),
    (1700, False),
    (1800, False),
    (1900, False),
    (2000, True),
    (2100, False),
    (2200, False),
    (2300, False),
    (2400, True),
    (2800, True),
    (2801, False),
]

if __name__ == "__main__":
    test_output(test_data, is_leap_year, True)
