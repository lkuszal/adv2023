import test_inputs.day03 as test_inputs
import re


def sum_all_engine_parts(parts_map):
    map_length_y = len(parts_map) - 1
    map_length_x = len(parts_map[0]) - 1
    solution = 0
    current_number = None
    for j, y in enumerate(parts_map):
        for i, x in enumerate(y):
            if current_number:
                if x.isnumeric():
                    current_number += x
                else:
                    number_end_x = i - 1
                    if check_if_engine_part(parts_map, number_y, number_start_x, number_end_x, map_length_y,
                                            map_length_x):
                        solution += int(current_number)
                    current_number = None
            elif x.isnumeric():
                current_number = x
                number_start_x = i
                number_y = j
        if current_number:
            number_end_x = map_length_x
            if check_if_engine_part(parts_map, number_y, number_start_x, number_end_x, map_length_y,
                                    map_length_x):
                solution += int(current_number)
            current_number = None
    return solution


def check_if_engine_part(parts_map, number_y, number_start_x, number_end_x, map_length_y, map_length_x):
    symbol_regex = r"[^0-9.\n]"
    if number_start_x != 0:
        number_start_x -= 1
    if number_end_x != map_length_x:
        number_end_x += 1
    if number_y != 0:
        part_to_check = parts_map[number_y - 1][number_start_x:number_end_x + 1]
        if re.findall(symbol_regex, part_to_check):
            return True
    part_to_check = parts_map[number_y][number_start_x:number_end_x + 1]
    if re.findall(symbol_regex, part_to_check):
        return True
    if number_y != map_length_y:
        part_to_check = parts_map[number_y + 1][number_start_x:number_end_x + 1]
        if re.findall(symbol_regex, part_to_check):
            return True


def test():
    for test_case in test_inputs.test_inputs_1:
        print(test_case)
        assert sum_all_engine_parts(test_case[0]) == test_case[1]

    for test_case in test_inputs.test_inputs_2:
        print(test_case)
        assert sum_gear_ratio(test_case[0]) == test_case[1]
    print('test passed')


def sum_gear_ratio(parts_map):
    map_length_y = len(parts_map) - 1
    map_length_x = len(parts_map[0]) - 1
    solution = 0
    for j, y in enumerate(parts_map):
        for i, x in enumerate(y):
            if x == '*':
                number_x = i
                number_y = j
                solution += get_gear_ratio(parts_map, number_y, number_x, map_length_y, map_length_x)
    return solution


def get_gear_ratio(parts_map, number_y, number_x, map_length_y, map_length_x):
    values = []
    left_side_available = number_x != 0
    right_side_available = number_x != map_length_x
    if number_y != 0:
        previous_line = iter_line(parts_map[number_y - 1])
        for key, value in previous_line.items():
            if left_side_available:
                if number_x - 1 in key:
                    values.append(value)
                    continue
            if number_x in key:
                values.append(value)
                continue
            if right_side_available:
                if number_x + 1 in key:
                    values.append(value)
                    continue

    if number_y != map_length_y:
        next_line = iter_line(parts_map[number_y + 1])
        for key, value in next_line.items():
            if left_side_available:
                if number_x - 1 in key:
                    values.append(value)
                    continue
            if number_x in key:
                values.append(value)
                continue
            if right_side_available:
                if number_x + 1 in key:
                    values.append(value)
                    continue

    current_line = iter_line(parts_map[number_y])
    for key, value in current_line.items():
        if left_side_available:
            if number_x - 1 in key:
                values.append(value)
                continue
        if right_side_available:
            if number_x + 1 in key:
                values.append(value)
                continue

    if len(values) == 2:
        return values[0] * values[1]
    else:
        return 0


def iter_line(line):
    current_number = ''
    current_positions = []
    position_to_number = {}
    for i, character in enumerate(line):
        if character.isnumeric():
            current_number += character
            current_positions.append(i)
        else:
            if current_number:
                position_to_number[range(current_positions[0], current_positions[-1] + 1)] = int(current_number)
                current_number = ''
                current_positions = []
    if current_number:
        position_to_number[range(current_positions[0], current_positions[-1] + 1)] = int(current_number)
    return position_to_number


test()
print(sum_all_engine_parts(
    open("C:\\Users\\Latul\\PycharmProjects\\adv2023\\inputs\\day03.txt", 'r').read().splitlines()))
print(sum_gear_ratio(
    open("C:\\Users\\Latul\\PycharmProjects\\adv2023\\inputs\\day03.txt", 'r').read().splitlines()))