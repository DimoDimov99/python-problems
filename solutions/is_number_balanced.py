from utils.test_program_output import test_output


def number_to_list(number):
    digit_list = []

    while number != 0:
        digit = number % 10
        digit_list.append(digit)
        number = number // 10
    return digit_list[::-1]


def is_number_balanced(number):
    left_part = 0
    right_part = 0
    digit_list = number_to_list(number)
    digit_list_len = len(digit_list)

    if digit_list_len % 2 == 0: # handle even number len
        middle = digit_list_len // 2
        for digit in range(digit_list_len):
            if digit + 1 <= middle:
                left_part += digit_list[digit]
            else:
                right_part += digit_list[digit]

    elif digit_list_len % 2 != 0: #handle odd number len
        middle = (digit_list_len // 2) + 1
        for digit in range(digit_list_len):
            if digit + 1 < middle:
                left_part += digit_list[digit]
            elif digit + 1 == middle:
                pass
            else:
                right_part += digit_list[digit]
    return left_part == right_part


test_data = [
    (True, 9),
    (True, 4518),
    (False, 28471),
    (True, 1238033),
    (False, 21111),

]


if __name__ == "__main__":
    test_output(test_data, is_number_balanced, True)
