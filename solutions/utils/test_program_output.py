DELIMITER = "-" * 60


def test_output(test_data, func, show_detailed_output=False, func_args=1):
    input_data_index = 1
    for _input, actual in test_data:
        tmp = _input  # saving input argument
        if func_args == 1:
            _input = func(_input)

        if func_args == 2:
            _input = func(_input[0], _input[1])

        if show_detailed_output:
            print(
                f"TEST CASE: [{input_data_index}] RESULT: [{_input == actual}], EXPECTED: '{actual}' | ACTUAL: '{_input}'\nPROVIDED INPUT: {tmp}")
            print(f"{DELIMITER}\n")
        else:
            print(
                f"TEST CASE: [{input_data_index}] RESULT: [{_input == actual}]")
        input_data_index += 1
