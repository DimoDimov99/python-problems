from utils.test_program_output import test_output


def roman_to_decimal(roman_letters):
    ROMAN_DIGITS = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    i = 0
    result = 0
    roman_letters_len = len(roman_letters)

    while i < roman_letters_len:
        if (
            i + 1 < roman_letters_len
            and ROMAN_DIGITS[roman_letters[i + 1]] > ROMAN_DIGITS[roman_letters[i]]
        ):
            result += (
                ROMAN_DIGITS[roman_letters[i + 1]] - ROMAN_DIGITS[roman_letters[i]]
            )
            i += 2
        else:
            result += ROMAN_DIGITS[roman_letters[i]]
            i += 1
    return result


test_data = [
    ("X", 10),
    ("V", 5),
    ("VI", 6),
    ("IV", 4),
    ("XXIV", 24),
    ("MMIV", 2004),
]


if __name__ == "__main__":
    test_output(test_data, roman_to_decimal, True)
