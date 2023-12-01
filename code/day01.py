import test_inputs.day01 as test_inputs
import re


def extract_calibration_value(input_line):
    first_digit_regex = r"(\d).*"
    last_digit_regex = r".*(\d)"
    first_digit = re.findall(first_digit_regex, input_line)[0]
    last_digit = re.findall(last_digit_regex, input_line)[0]
    return int(str(first_digit) + str(last_digit))


def extract_and_sum_calibration_values():
    solution = 0
    with open('/Users/latul/adv2023/inputs/day01.txt') as final_input:
        for line in final_input.readlines():
            solution += extract_calibration_value(line)
    print(solution)


def extract_calibration_value_with_words(input_line):
    word_to_digit_map = {'zero': 0,
                         "one": 1,
                         "two": 2,
                         "three": 3,
                         "four": 4,
                         "five": 5,
                         "six": 6,
                         "seven": 7,
                         "eight": 8,
                         "nine": 9}
    first_digit_regex = r"(\d|zero|one|two|three|four|five|six|seven|eight|nine).*"
    last_digit_regex = r".*(\d|zero|one|two|three|four|five|six|seven|eight|nine)"
    first_digit = re.findall(first_digit_regex, input_line)[0]
    last_digit = re.findall(last_digit_regex, input_line)[0]
    if len(first_digit) > 1:
        first_digit = word_to_digit_map[first_digit]
    if len(last_digit) > 1:
        last_digit = word_to_digit_map[last_digit]
    return int(str(first_digit) + str(last_digit))

def extract_and_sum_calibration_values_with_words():
    solution = 0
    with open('/Users/latul/adv2023/inputs/day01.txt') as final_input:
        for line in final_input.readlines():
            solution += extract_calibration_value_with_words(line)
    print(solution)

def test():
    for test in test_inputs.test_inputs_1:
        print(test)
        assert extract_calibration_value(test[0]) == test[1]
    print('test passed')

    for test in test_inputs.test_inputs_2:
        print(test)
        assert extract_calibration_value_with_words(test[0]) == test[1]
    print('test passed')


test()
print(extract_and_sum_calibration_values())
print(extract_and_sum_calibration_values_with_words())