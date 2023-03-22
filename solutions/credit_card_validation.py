from utils.test_program_output import test_output

test_data = [
    (79927398713, True),
    (4417123456789113, True),
    (4242424242424242, True),
    (79927398715, False),
    (79927398710, False),
    (79927398711, False),
    (79927398712, False),
    (79927398714, False),
    (79927398715, False),
    (79927398716, False),
    (79927398717, False),
    (79927398718, False),
    (79927398719, False)
]


def number_to_list(number):
    result = []

    while number != 0:
        digit = number % 10
        result.append(digit)
        number = number // 10

    return result


def sum_of_digits(number):
    total = 0

    while number != 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total


def is_credit_card_valid(number):
    # Luhn algorithm
    number_to_check = 0
    digit_list = number_to_list(number)

    for i in range(0, len(digit_list)):
        if i % 2 == 0:
            number_to_check += digit_list[i]
        else:
            tmp = digit_list[i] * 2
            if tmp >= 10:
                tmp = sum_of_digits(tmp)
                number_to_check += tmp
            else:
                number_to_check += tmp
    return number_to_check % 10 == 0


if __name__ == "__main__":
    test_output(test_data, is_credit_card_valid, True)
