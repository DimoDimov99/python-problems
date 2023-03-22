from utils.test_program_output import test_output


def palindromes_count(number):
    numbers_list = []
    palindrome_counter = 0

    for n in range(10, number + 1):
        numbers_list.append(str(n))

    for n in numbers_list:
        rev_number = n[::-1]
        if n == rev_number:
            palindrome_counter += 1

    return palindrome_counter


test_data = [
    (10, 0),
    (20, 1),
    (101, 10),
    (92009, 1009),
    (99999, 1089),
]


if __name__ == "__main__":
    test_output(test_data, palindromes_count, True)
