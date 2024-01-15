from utils.test_program_output import test_output
from credit_card_validation import is_credit_card_valid


def censor_credit_card_numbers(_input):
    check_is_valid = is_credit_card_valid(_input)
    if check_is_valid:
        credit_card_to_str = str(_input)
        censor_len = len(credit_card_to_str) - 4
        asterics = "*" * censor_len
        result = asterics + credit_card_to_str[censor_len:]
        return result
    return False


test_data = [
    (4417123456789113, "************9113"),
    (4242424242424242, "************4242"),
    (79927398715, False),
]

if __name__ == "__main__":
    test_output(test_data, censor_credit_card_numbers, True)
