from utils.test_program_output import test_output


def to_camel_case(text):
    # Terrible solution, but it works :D I will improve
    to_list = []
    camel_indexes = []
    diff = 0
    for i in range(len(text)):
        if text[i] != "_" and text[i] != "-":
            to_list.append(text[i])
        else:
            camel_indexes.append(i)
    for i in range(len(camel_indexes)):
        to_list[camel_indexes[i] - diff] = to_list[camel_indexes[i] - diff].title()
        diff += 1

    return "".join(to_list)


test_data = [
    ("the-stealth-warrior", "theStealthWarrior"),
    ("The_Stealth_Warrior", "TheStealthWarrior"),
    ("The_Stealth-Warrior", "TheStealthWarrior"),
    ("A_pippi-was_cute", "APippiWasCute"),
    ("a-pippi_Is_pippi", "aPippiIsPippi"),
]

if __name__ == "__main__":
    test_output(test_data, to_camel_case, True)
