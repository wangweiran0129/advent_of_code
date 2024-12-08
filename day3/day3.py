import re
import sys
sys.path.insert(0, "../")
from general import *


def is_valid_mul(input_content):
    
    pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
    matches = re.findall(pattern, input_content)
    
    return matches


def is_val_mul_ins(input_content):

    pattern = r"do\(\)|don't\(\)|mul\((-?\d+),\s*(-?\d+)\)"
    matches = re.finditer(pattern, input_content)

    state = True
    valid_mul = []  # List to store valid mul instructions

    for match in matches:
        full_match = match.group(0)

        if full_match == "do()":
            state = True
        elif full_match == "don't()":
            state = False
        else:
            # Handle mul(X,Y)
            x, y = int(match.group(1)), int(match.group(2))
            if state:
                valid_mul.append((x, y))

    return valid_mul


def mul(matches):

    final_res = 0

    for mul_ele in matches:
        final_res = final_res + (int(mul_ele[0]) * int(mul_ele[1]))
    
    return final_res


if __name__ == "__main__":
    
    input_file = "input.txt"
    input_content = read_input(input_file)

    # # Part 1
    # matches = is_valid_mul(input_content)
    # result = mul(matches)
    # print("The result of Part 1: ", result)

    # Part 2
    valid_matches = is_val_mul_ins(input_content)
    result = mul(valid_matches)
    print("The result of Part 2: ", result)