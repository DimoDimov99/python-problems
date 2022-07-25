from utils.test_program_output import test_output



def to_digits(number):
    digit_list = []

    while number != 0:
        digit = number % 10
        digit_list.append(digit)
        number = number // 10

    return digit_list[::-1]

test_data = [
    ([1, 2, 3], 123),
    ([9, 9, 9, 9, 9], (99999)),
    ([1, 2, 3, 0, 2, 3], (123023))
]

if __name__ == "__main__":
    test_output(test_data, to_digits, True)