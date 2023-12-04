import test_inputs.day04 as test_inputs
import re


def test():
    for test_case in test_inputs.test_inputs_1:
        print(test_case)
        assert count_scratchcard_point(test_case[0]) == test_case[1]
    print('test passed')

    for test_case in test_inputs.test_inputs_2:
        print(test_case)
        assert count_number_of_all_scratchcards(test_case[0].split('\n')) == test_case[1]
    print('test passed')


def sum_scratchcard_points():
    solution = 0
    with open('/Users/latul/adv2023/inputs/day04.txt') as final_input:
        for line in final_input.readlines():
            solution += count_scratchcard_point(line)
    print(solution)


def count_scratchcard_point(scratchcard):
    won_numbers = count_number_of_matches(scratchcard)
    if won_numbers == 0:
        return 0
    else:
        return 2 ** (won_numbers - 1)


def count_number_of_matches(scratchcard):
    winning_numbers, card_numbers = scratchcard.split(':')[1].split('|')
    return len(set(winning_numbers.split()) & set(card_numbers.split()))


def count_number_of_all_scratchcards(scratchcards):
    number_of_cards = 0
    number_of_duplicates = {}
    for game_number, line in enumerate(scratchcards):
        if game_number in number_of_duplicates.keys():
            current_duplicates = number_of_duplicates[game_number]
        else:
            current_duplicates = 1
        number_of_cards += current_duplicates
        number_of_wins = count_number_of_matches(line)
        for i in range(number_of_wins):
            updated_game_number = game_number + i + 1
            if updated_game_number in number_of_duplicates.keys():
                number_of_duplicates[updated_game_number] = number_of_duplicates[updated_game_number] + current_duplicates
            else:
                number_of_duplicates[updated_game_number] = current_duplicates + 1
    return number_of_cards

test()
sum_scratchcard_points()
with open('/Users/latul/adv2023/inputs/day04.txt') as final_input:
    print(count_number_of_all_scratchcards(final_input.readlines()))