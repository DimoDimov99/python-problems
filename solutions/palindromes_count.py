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
    (0, 10),
    (1, 20),
    (10, 101),
    (1009, 92009),
    (1089, 99999),
]


if __name__ == "__main__":
    test_output(test_data, palindromes_count, True)
