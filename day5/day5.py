import sys
sys.path.insert(0, "../")
from general import *


def split_first_section_section(input_content):

    grid = input_content.strip().splitlines()

    split_index = grid.index('')
    first_section = grid[:split_index]
    sec_section = grid[split_index+1:]
    second_section = []

    for i in sec_section:
        second_section.append(i.split(','))

    return first_section, second_section
        

def is_incorrect_order(first_section, update):

    for i in range(0, len(update)-1):
        for j in range(i+1, len(update)):
            rule = str(update[i] + '|' + update[j])
            if rule not in first_section:
                return True

    return False
            

def correct_and_incorrect_updates(first_section, second_section):

    correct_updates = []
    incorrect_updates = []

    for update in second_section:
        if not is_incorrect_order(first_section, update):
            correct_updates.append([int(element) for element in update])
        else:
            incorrect_updates.append([int(element) for element in update])
                
    return correct_updates, incorrect_updates


def cal_sum_middle_num(updates):

    sum = 0
    
    for update in updates:
        sum += update[len(update)//2]

    return sum


def fix_incorrect_updates(incorrect_updates, first_section):

    fixed_updates = []
    for incorrect_update in incorrect_updates:
        for i in range(0, len(incorrect_update)-1):
            for j in range(i+1, len(incorrect_update)):
                rule = str(incorrect_update[i]) + '|' + str(incorrect_update[j])
                if rule not in first_section:
                    incorrect_update[i], incorrect_update[j] = incorrect_update[j], incorrect_update[i]
        fixed_updates.append([int(element) for element in incorrect_update])
    
    return fixed_updates


if __name__ == "__main__":
    
    input_file = "input.txt"
    input_content = read_input(input_file)

    first_section, second_section = split_first_section_section(input_content)
    correct_updates, incorrect_updates = correct_and_incorrect_updates(first_section, second_section)
    part1_result = cal_sum_middle_num(correct_updates)
    print("Part 1 result: ", part1_result)

    fixed_updates = fix_incorrect_updates(incorrect_updates, first_section)
    part2_result = cal_sum_middle_num(fixed_updates)
    print("Part 1 result: ", part2_result)