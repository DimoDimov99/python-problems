from utils.test_program_output import test_output

def factorial(number):
    if number == 0:
        return 1

    fact = 1

    while number > 0:
        fact = number * fact
        number = number - 1
    return fact


def fact_digits(number):
    number = abs(number)
    _sum = 0

    while number != 0:
        digit = number % 10
        _sum += factorial(digit)
        number = number // 10

    return _sum


test_data = [
    (3, 101),
    (3, 111),
    (145, 145),
    (1088640, 999),
]


if __name__ == "__main__":
    test_output(test_data,fact_digits)
