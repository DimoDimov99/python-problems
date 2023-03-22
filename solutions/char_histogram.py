from utils.test_program_output import test_output


def char_histogram(string):
    result = {}

    for character in string:
        if character not in result:
            result[character] = 0

        result[character] += 1

    return result


test_data = [
    ("", {}),
    ("    ", {" ": 4}),
    ("Dimo", {'D': 1, 'i': 1, 'm': 1, 'o': 1}),
    ("AAAAaaa!!!", {'A': 4, 'a': 3, '!': 3}),
]

if __name__ == "__main__":
    test_output(test_data, char_histogram, True)
