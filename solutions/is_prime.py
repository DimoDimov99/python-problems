from utils.test_program_output import test_output


def is_prime(number):
    if number <= 1:
        return False

    for divisior in range(2, number):
        if number % divisior == 0:
            return False
    return True


test_data = [(1, False), (2, True), (8, False), (11, True), (-10, False)]


if __name__ == "__main__":
    test_output(test_data, is_prime, True)
