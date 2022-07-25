DELIMITER = "-" * 60


def test_output(test_data, func, show_detailed_output=False, func_args=1):
    input_data_index = 1
    index = 0
    for expected, actual in test_data:
        if func_args == 1:
            actual = func(actual)

        if func_args == 2:
            actual = func(actual[0], actual[1])

        if show_detailed_output:
            print(f"TEST CASE: [{input_data_index}] RESULT: [{expected == actual}], EXPECTED: '{expected}' | ACTUAL: '{actual}'\nPROVIDED INPUT: {test_data[index][1]}")
            print(f"{DELIMITER}\n")
        else:
            print(f"TEST CASE: [{input_data_index}] RESULT: [{expected == actual}]")
        index += 1
        input_data_index += 1



def test():
    print("Test")