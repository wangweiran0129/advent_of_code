import sys
sys.path.insert(0, "../")
from general import *
from itertools import product


def evaluate_left_to_right(numbers, operators):

    result = numbers[0]

    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i+1]
        elif operators[i] == '*':
            result *= numbers[i+1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i+1]))
    
    return result


def can_produce_test_value(test_value, numbers):

    operator_combinations = product(['+', '*', '||'], repeat=len(numbers)-1)
    
    for operators in operator_combinations:
        if evaluate_left_to_right(numbers, operators) == test_value:
            return True
    
    return False


def calculate_total_calibration(input_lines):

    total_calibration = 0

    for line in input_lines:
        test_value, number_str = line.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, number_str.strip().split()))

        if can_produce_test_value(test_value, numbers):
            total_calibration += test_value
    
    return total_calibration



if __name__ == "__main__":
    input_file = 'input.txt'
    input_content = read_input(input_file)
    grid = input_content.strip().splitlines()

    # Part 1
    part1_answer = calculate_total_calibration(grid)
    print("The answer of part 1: ", part1_answer)

    # Part 2
