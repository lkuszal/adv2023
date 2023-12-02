import test_inputs.day02 as test_inputs
import re

all_cubes = {"red": 12, "green": 13, "blue": 14}
all_red_gems_in_game_regex = r"(\d*) red"
all_green_gems_in_game_regex = r"(\d*) green"
all_blue_gems_in_game_regex = r"(\d*) blue"


def check_if_game_is_possible(game_input):
    highest_red_number = max([int(i) for i in re.findall(all_red_gems_in_game_regex, game_input)])
    highest_green_number = max([int(i) for i in re.findall(all_green_gems_in_game_regex, game_input)])
    highest_blue_number = max([int(i) for i in re.findall(all_blue_gems_in_game_regex, game_input)])
    return (all_cubes["red"] >= highest_red_number and
            all_cubes["green"] >= highest_green_number and
            all_cubes["blue"] >= highest_blue_number)


def parse_input_and_sum_possible_games():
    game_number_regex = r"Game (\d*)"
    solution = 0
    with open("C:\\Users\\Latul\\PycharmProjects\\adv2023\\inputs\\day02.txt") as final_input:
        for line in final_input.readlines():
            if check_if_game_is_possible(line):
                solution += int(re.findall(game_number_regex, line)[0])
    print(solution)


def multiply_highest_number_of_each_color(game_input):
    highest_red_number = max([int(i) for i in re.findall(all_red_gems_in_game_regex, game_input)])
    highest_green_number = max([int(i) for i in re.findall(all_green_gems_in_game_regex, game_input)])
    highest_blue_number = max([int(i) for i in re.findall(all_blue_gems_in_game_regex, game_input)])
    return highest_red_number * highest_green_number * highest_blue_number


def parse_input_and_sum_multiplied_highest_number_of_colors():
    solution = 0
    with open("C:\\Users\\Latul\\PycharmProjects\\adv2023\\inputs\\day02.txt") as final_input:
        for line in final_input.readlines():
            solution += multiply_highest_number_of_each_color(line)
    print(solution)


def test():
    for test_case in test_inputs.test_inputs_1:
        print(test_case)
        assert check_if_game_is_possible(test_case[0]) == test_case[1]

    for test_case in test_inputs.test_inputs_2:
        print(test_case)
        assert multiply_highest_number_of_each_color(test_case[0]) == test_case[1]
    print('test passed')


test()
parse_input_and_sum_possible_games()
parse_input_and_sum_multiplied_highest_number_of_colors()
