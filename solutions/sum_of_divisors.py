from utils.test_program_output import test_output


def sum_of_divisors(number):
    divisors_sum = 0

    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors_sum += divisor

    return divisors_sum


test_data = [
    (8, 15),
    (7, 8),
    (1, 1),
    (1000, 2340),
]


if __name__ == "__main__":
    test_output(test_data, sum_of_divisors, True)
