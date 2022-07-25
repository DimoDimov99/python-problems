from utils.test_program_output import test_output


def count_substrings(haystack, needle):
    haystack_len = len(haystack)
    temp_str = ""
    tempt_counter = 0
    total_occurances = 0


    for i in range(haystack_len):
        if haystack[i] == needle[tempt_counter]:
            temp_str += haystack[i]
            tempt_counter += 1

        elif haystack[i] != needle[tempt_counter]:
            temp_str = ""
            tempt_counter = 0

        if temp_str == needle:
            total_occurances += 1
            tempt_counter = 0
            temp_str = ""

    return total_occurances



test_data = [
    (2, ("This is a test string", "is")),
    (2, ("babababa", "baba")),
    (4, ("Python is an awesome language to program in!", "o")),
    (0, ("We have nothing in common!", "really?")),
    (2, ("This is this and that is this that is", "this")),
    (0, ("That that is", "this")),
    (3, ("Dimodimodimodimo", "dimo"))
]


if __name__ == "__main__":
    test_output(test_data, count_substrings, True, 2)
