from utils.test_program_output import test_output


def digit_sum(n):
    digit_sum = 0
    while n != 0:
        digit = n % 10
        digit_sum += digit
        n = n // 10
    return digit_sum


def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(digit_sum(n))


def digital_root2(n):
    return n % 9 or n and 9


test_data = [(16, 7), (942, 6), (132189, 6), (493193, 2)]

if __name__ == "__main__":
    test_output(test_data, digital_root, True)
    # test_output(test_data, digital_root2, True)
