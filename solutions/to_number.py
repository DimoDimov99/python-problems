from utils.test_program_output import test_output


def to_number(digits):
    digits_to_number = 0
    # reverse the list in order to get the correct starting order
    digits = digits[::-1]
    for i in range(len(digits)):
        digit = digits[i] * (10 ** i)
        digits_to_number += digit

    return digits_to_number


def to_number2(digits):
    """tricky solution without involving the beauty of math"""
    number = ""
    for i in digits:
        number += str(i)

    return int(number)


test_data = [
    ([1, 2, 3], 123),
    ([9, 9, 9, 9, 9], 99999),
    ([1, 2, 3, 0, 2, 3], 123023),
    ([2, 1, 2, 3, 3], 21233),
]

if __name__ == "__main__":
    test_output(test_data, to_number, True)
    # test_output(test_data, to_number2)
