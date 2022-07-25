from utils.test_program_output import test_output


def to_number(digits):
    digits_to_number = 0
    digits = digits[::-1] # reverse the list in order to get the correct starting order
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
    (123, [1, 2, 3]),
    (99999, [9, 9, 9, 9, 9]),
    (123023, [1, 2, 3, 0, 2, 3]),
    (21233, [2, 1, 2, 3, 3]),
]

if __name__ == "__main__":
    test_output(test_data, to_number)
    # test_output(test_data, to_number2)
