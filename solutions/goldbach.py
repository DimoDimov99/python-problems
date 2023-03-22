from utils.test_program_output import test_output

test_data = [
    (4, [(2, 2)]),
    (6, [(3, 3)]),
    (8, [(3, 5)]),
    (10, [(3, 7), (5, 5)]),
    (100, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]),
    (5, None)
]


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def goldbach(number):
    if number % 2 != 0:
        return None
    result = []
    duplicates = set()

    for i in range(2, number):
        for j in range(2, number):
            if is_prime(i) and is_prime(j):
                if i + j == number:
                    pair = (i, j)
                    rev_pair = (j, i)
                    if pair not in duplicates and rev_pair not in duplicates:
                        duplicates.add(pair)
                        result.append(pair)
    return result


if __name__ == "__main__":
    test_output(test_data, goldbach, True)
