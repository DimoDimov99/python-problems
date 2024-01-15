from utils.test_program_output import test_output


def add_two_nums(num1, num2):
    return num1 + num2


def multiple_two_nums(num1, num2):
    return num1 * num2


def compare_two_numbers(num1, num2):
    return num1 == num2


def return_three_numbers(num1, num2, num3):
    return num1, num2, num3


# test_data = [([5, 6], 5), ([2, 2], 4)]
test_data_add_two_nums = [((1, 2), 3)]
test_data_multiple_two_nums = [((1, 2), 2), ((2, 2), 50)]


if __name__ == "__main__":
    print(f"Func: add_two_nums():\n")
    test_output(test_data_add_two_nums, add_two_nums, True, 2)
    print(f"\nFunc: multiple_two_nums():\n")
    test_output(test_data_multiple_two_nums, multiple_two_nums, True, 2)
