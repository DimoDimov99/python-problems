# Colors
FAIL = "\033[91m"
OKGREEN = "\033[92m"
RESET = "\033[0m"

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

        elif func_args == 2:
            _input = func(_input[0], _input[1])

        elif func_args == 3:
            _input = func(_input[0], _input[1], _input[2])

        if expected == _input:
            total_pass_tc += 1
            total_pass_tc_string += (
                f"\nTEST CASE [{input_data_index}] {OKGREEN}[PASS]{RESET}"
            )
        else:
            total_fail_tc += 1
            total_fail_tc_string += (
                f"\nTEST CASE [{input_data_index}] {FAIL}[FAIL]{RESET}"
            )
        if show_detailed_output:
            color = ""
            check = _input == expected
            check_txt = ""
            if check:
                color = OKGREEN
                check_txt = f"{OKGREEN}[{expected} == {_input}]{RESET}"
            else:
                color = FAIL
                check_txt = f"{FAIL}[{expected} != {_input}]{RESET}"
            print(
                f"TEST CASE: [{input_data_index}] EXPECTED: '{expected}' | ACTUAL: '{_input}', RESULT: {check_txt} {color}[{_input == expected}]{RESET} \nPROVIDED INPUT: {tmp}"
            )
            print(f"{DELIMITER}")
        else:
            print(f"TEST CASE: [{input_data_index}] RESULT: [{_input == expected}]")
            print(f"{DELIMITER}")
        input_data_index += 1
    print(
        f"Total passing TC: {OKGREEN}[{total_pass_tc}]{RESET} {total_pass_tc_string}\n{DELIMITER}"
    )
    if total_fail_tc > 0:
        print(
            f"Total failing TC: {FAIL}[{total_fail_tc}]{RESET} {total_fail_tc_string}{RESET}"
        )
    else:
        # if no failures
        print(
            f"Total failing TC: {OKGREEN}[{total_fail_tc}] {total_fail_tc_string}{RESET}"
        )
    print(f"{DELIMITER}")
