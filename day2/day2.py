def read_input(input_file):

    with open(input_file, "r") as file:
        content = file.read()

    return content


def is_increasing(int_row):
    return all(int_row[i] < int_row[i + 1] for i in range(len(int_row) - 1))


def is_decreasing(int_row):
    return all(int_row[i] > int_row[i + 1] for i in range(len(int_row) - 1))


def is_difference_within_range(int_row):

    min_diff = 1
    max_diff = 3

    return all(min_diff <= abs(int_row[i]-int_row[i+1]) <= max_diff for i in range(len(int_row)-1))


def count_safe_report(input_content):
    
    count = 0

    rows = [line.split() for line in input_content.strip().split("\n")]

    for row in rows:
        int_row = list(map(int, row))
        if is_increasing(int_row) or is_decreasing(int_row): 
            if is_difference_within_range(int_row):
                count += 1

    return count


def making_increasing_or_decreasing(int_row):

    for i in range(len(int_row)):
        modified_list = int_row[:i] + int_row[i+1:]
        if is_increasing(modified_list) or is_decreasing(modified_list):
            return modified_list
    
    return False


def making_difference_within_range(int_row):

    for i in range(len(int_row)):
        modified_list = int_row[:i] + int_row[i+1:]
        if is_difference_within_range(modified_list) and (is_increasing(modified_list) or is_decreasing(modified_list)):
            return True
    
    return False


def install_problem_damener(input_content):
    
    count = 0

    rows = [line.split() for line in input_content.strip().split("\n")]

    for row in rows:
        int_row = list(map(int, row))

        if is_increasing(int_row) or is_decreasing(int_row) or making_increasing_or_decreasing(int_row): 
            if is_difference_within_range(int_row) or making_difference_within_range(int_row):
                count += 1

    return count


if __name__ == "__main__":
    input_file = "puzzle_input.txt"
    input_content = read_input(input_file)

    # Part 1
    number_of_safe_reports = count_safe_report(input_content)
    print("How many reports are safe?", number_of_safe_reports)

    # Part 2
    number_of_safe_reports_after_damener = install_problem_damener(input_content)
    print("How many reports are safe after installing the damener?", number_of_safe_reports_after_damener)
