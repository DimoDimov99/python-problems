DELIMITER = "-" * 60


def test_output(test_data, func, show_detailed_output=False, func_args=1):
    input_data_index = 1
    total_pass_tc = 0
    total_fail_tc = 0
    total_pass_tc_string = ""
    total_fail_tc_string = ""
    for _input, expected in test_data:
        tmp = _input  # saving input argument
        if func_args == 1:
            _input = func(_input)

        if func_args == 2:
            _input = func(_input[0], _input[1])

        if expected == _input:
            total_pass_tc += 1
            total_pass_tc_string += f"\nTEST CASE [{input_data_index}] PASS"
        else:
            total_fail_tc += 1
            total_fail_tc_string += f"\nTEST CASE [{input_data_index}] FAIL"
        if show_detailed_output:
            print(
                f"TEST CASE: [{input_data_index}] EXPECTED: '{expected}' | ACTUAL: '{_input}', RESULT: [{_input == expected}]\nPROVIDED INPUT: {tmp}"
            )
            print(f"{DELIMITER}")
        else:
            print(f"TEST CASE: [{input_data_index}] RESULT: [{_input == expected}]")
            print(f"{DELIMITER}")
        input_data_index += 1
    print(
        f"Total passing TC: {total_pass_tc} {total_pass_tc_string}\n{DELIMITER}\nTotal failing TC: {total_fail_tc} {total_fail_tc_string}"
    )
    print(f"{DELIMITER}")
