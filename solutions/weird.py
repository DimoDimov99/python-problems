from utils.test_program_output import test_output


def weird(_input):
    if _input % 2 != 0:
        return "Weird"
    elif _input % 2 == 0 and _input >= 2 and _input <= 5:
        return "Not Weird"
    elif _input % 2 == 0 and _input >= 6 and _input <= 20:
        return "Weird"
    elif _input % 2 == 0 and _input > 20:
        return "Not Weird"


test_data = [
    (3, "Weird"),
    (4, "Not Weird"),
    (6, "Weird"),
    (24, "Not Weird"),
    (21, "Weird"),
]

if __name__ == "__main__":
    test_output(test_data, weird, True)
