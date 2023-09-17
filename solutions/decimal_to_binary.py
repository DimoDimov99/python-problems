from utils.test_program_output import test_output


def decimal_to_binary(decimal):
    result = ""
    if decimal == 0:
        return 0
    while decimal != 0:
        if decimal % 2 == 0:
            decimal = decimal // 2
            result += "0"
        else:
            decimal = decimal // 2
            result += "1"
    return int(result[::-1])


test_data = [(0, 0), (2, 10), (3, 11), (4, 100), (256, 100000000), (6, 110)]

if __name__ == "__main__":
    test_output(test_data, decimal_to_binary, True)
