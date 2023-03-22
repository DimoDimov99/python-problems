from utils.test_program_output import test_output


def anagrams(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    return sorted(word1) == sorted(word2)


tests = [
    (("silent", "listen"), True),
    (("SILENT", "listen"), True),
    (("silent", "LISTEN"), True),
    (("python", "ruby"), False),
    (("a gentleman", "elegant man"), True),
    (("eleven plus two", "twelve plus one"), True),
    (("William Shakespeare", "I am a weakish speller"), True),
    (("", ""), True)
]


def test_func(test_data):
    for actual, expected in test_data:
        result = anagrams(*actual)
        print(result == expected)


if __name__ == "__main__":
    test_func(tests)
