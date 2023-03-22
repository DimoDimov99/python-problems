from utils.test_program_output import test_output


def iban_formatter(iban):
    counter = 0
    result = []
    for character in iban:
        if character == " ":
            continue
        result.append(character)
        counter += 1

        if counter == 4:
            result.append(" ")
            counter = 0

    result = "".join(result)
    return result


test_data = [
    ("BG80BNBG96611020345678", "BG80 BNBG 9661 1020 3456 78"),
    ("BG80 BNBG 9661 1020 3456 78", "BG80 BNBG 9661 1020 3456 78"),
    ("BG14TTBB94005362446381", "BG14 TTBB 9400 5362 4463 81"),
    ("BG14 TTBB 9400 5362 4463 81", "BG14 TTBB 9400 5362 4463 81"),
    ("BG91UNCR70001864961754", "BG91 UNCR 7000 1864 9617 54"),
    ("BG91 UNCR 7000 1864 9617 54", "BG91 UNCR 7000 1864 9617 54")
]


if __name__ == "__main__":
    test_output(test_data, iban_formatter, True)
