from utils.test_program_output import test_output


def fibonacci_number(number):
    prev_number = 0
    current_number = 1
    if number < 2:
        return number
    
    for _ in range(1, number):
        next_number = prev_number + current_number
        prev_number = current_number
        current_number = next_number
    return next_number


test_data = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (11, 89),
    (12, 144),
    (13, 233),
    (14, 377)
]

if __name__ == "__main__":
    test_output(test_data, fibonacci_number, True)