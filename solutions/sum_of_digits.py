from utils.test_program_output import test_output


def sum_of_digits(number):
    number = abs(number)
    _sum = 0

    while (number != 0):
        digit = number % 10
        _sum += digit
        number = number // 10
    return _sum


test_data = [
    (1325132435356, 43),
    (123, 6),
    (6, 6),
    (-10, 1),
]


if __name__ == "__main__":
    test_output(test_data, sum_of_digits, True)
