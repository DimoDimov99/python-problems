from utils.test_program_output import test_output


def perfect_number(number):
    temp = []
    for i in range(1, number):
        if number % i == 0:
            temp.append(i)
    return number == sum(temp)


test_data = [
    (6, True),
    (28, True),
    (496, True),
    (8128, True),
    # (33550336, True),
    (125, False),
    (369, False),
]

if __name__ == "__main__":
    test_output(test_data, perfect_number, True)
