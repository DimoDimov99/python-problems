from utils.test_program_output import test_output


def number_to_list(number):
    digit_list = []

    while number != 0:
        digit = number % 10
        digit_list.append(digit)
        number = number // 10

    return digit_list[::-1]


def contains_digits(number, digits):
    found = True

    digit_list = number_to_list(number)

    for digit in digits:
        if digit not in digit_list:
            return False

    return found


test_data = [
    ((402123, [0, 3, 4]), True),
    ((666, [6, 4]), False),
    ((1234567898, [1, 2, 3, 0]), False),
    ((456, []), True),
]


if __name__ == "__main__":
    test_output(test_data, contains_digits, True, 2)
