from utils.test_program_output import test_output


def char_histogram(string):
    result = {}

    for character in string:
        if character not in result:
            result[character] = 0

        result[character] += 1

    return result

test_data = [
    ({}, ""),
    ({" ": 4}, "    "),
    ({'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1}, "Python!"),
    ({'A': 4, 'a': 3, '!': 3}, "AAAAaaa!!!"),
    ({'S': 1,
    'o': 2,
    'm': 1,
    'e': 6,
    ' ': 7,
    'v': 1,
    'r': 4,
    'y': 1,
    'l': 1,
    'n': 4,
    'g': 3,
    's': 2,
    't': 3,
    'i': 4,
    'h': 2,
    'w': 1,
    'd': 1,
    'f': 2,
    'c': 1,
    'a': 1}, "Some very long string here with different casing")
]

if __name__ == "__main__":
    # print(char_histogram("Test"))
    test_output(test_data, char_histogram)
