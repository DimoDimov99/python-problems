from utils.test_program_output import test_output


def nan_expand(times):
    not_a = []
    if times <= 0:
        return ""
    for _ in range(times):
        not_a.append("Not a ")
    not_a.append("NaN")

    return "".join(not_a)


test_data = [
    ("", 0),
    ("Not a NaN", 1),
    ("Not a Not a NaN", 2),
    ("Not a Not a Not a NaN", 3)
]

if __name__ == "__main__":
    test_output(test_data, nan_expand)
