from utils.test_program_output import test_output


def is_prime(number):
    if number <= 1:
        return False

    for divisior in range(2, number):
        if number % divisior == 0:
            return False
    return True


test_data = [
    (False, 1),
    (True, 2),
    (False, 8),
    (True, 11),
    (False, -10)
]


if __name__ == "__main__":
    test_output(test_data, is_prime, True)
