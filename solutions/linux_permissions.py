from utils.test_program_output import test_output

BINARY_TO_DECIMAL = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7",
}

LINUX_PERMISSIONS = {
    "7": "rwx",
    "6": "rw-",
    "5": "r-x",
    "4": "r--",
    "3": "-wx",
    "2": "-w-",
    "1": "--x",
    "0": "---",
}


# from decimal to binary function
def to_binary(_input):
    _input = int(_input)
    if _input == 0:
        return "0"
    result = ""
    while _input != 0:
        if _input % 2 == 0:
            result += "0"
            _input = _input // 2
        else:
            result += "1"
            _input = _input // 2
    return result


# logic to transfer every digit from xxx to binary(3 symbol len)
def save_inputs(_input):
    _input = str(_input)
    t = ["0", "0", "0"]
    t_t = to_binary(_input)

    for i in range(len(t_t)):
        if t[i] != t_t[i]:
            t[i] = t_t[i]
    return t[::-1]


def parse_input(_input):
    _input = str(_input)
    _input_len = len(_input)
    if _input == "0":
        _input = "000"
        _input_len = 3
    t = []
    t_t = []
    tmp = ""
    result = ""

    # save input to t list
    for i in range(_input_len):
        t.append(_input[i])

    # nest into list, 3 list containing decimal number to binary
    for i in range(len(t)):
        t_t.append(save_inputs(t[i]))

    for i in range(len(t_t)):
        tmp = ""
        tmp = "".join(t_t[i])
        # create result, from BINARY_TO_DECIMAL dict, eg 111 -> 7
        result += BINARY_TO_DECIMAL[tmp]

    return result


def linux_permissions(_input):
    # handling invalid outputs, not the prettiest
    if len(str(_input)) < 3 and _input != 0 and _input < 100 or _input > 777:
        return -1
    parsed_input = parse_input(_input)
    result = ""

    for i in range(len(parsed_input)):
        if i == 0:
            result += f"\nOwner {LINUX_PERMISSIONS[parsed_input[i]]}\n"
        if i == 1:
            result += f"Group {LINUX_PERMISSIONS[parsed_input[i]]}\n"
        if i == 2:
            result += f"Others {LINUX_PERMISSIONS[parsed_input[i]]}"
    return result


test_data = [
    (000, "\nOwner ---\nGroup ---\nOthers ---"),
    (777, "\nOwner rwx\nGroup rwx\nOthers rwx"),
    (644, "\nOwner rw-\nGroup r--\nOthers r--"),
    (666, "\nOwner rw-\nGroup rw-\nOthers rw-"),
    (1, -1),
    (-1, -1),
    (778, -1),
]

if __name__ == "__main__":
    test_output(test_data, linux_permissions, True)
