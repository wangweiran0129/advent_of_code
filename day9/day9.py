import sys
sys.path.insert(0, "../")
from general import *


def convert_str_to_block(input_content):

    list_input = list(input_content)
    individual_block = []

    for idx, ele in enumerate(list_input):
        if idx%2 == 0:
            for i in range(0, int(ele)):
                individual_block.append(int(idx/2))
        else:
            for i in range(0, int(ele)):
                individual_block.append('.')

    return individual_block


def count_consecutive_digits(individual_block):

    count = 0
    for ele in individual_block:
        if ele == '.':
            break
        count += 1
    
    return count


def move_file_blocks(individual_block):

    # Count how many digits in the individual_block
    count = 0
    for ele in individual_block:
        if ele != '.':
            count += 1

    offset = -1
    for idx in range(0, len(individual_block)):
        if individual_block[idx] == '.':
            if count_consecutive_digits(individual_block) == count:
                break
            while individual_block[offset] == '.':
                offset -= 1
            individual_block[idx], individual_block[offset] = individual_block[offset], individual_block[idx]
            offset -= 1

    return individual_block


def cal_filesystem_checksum(individual_block):

    checksum = 0
    for idx, ele in enumerate(individual_block):
        if ele == '.':
            break
        checksum += idx * int(ele)
    
    return checksum


def identify_files_and_free_space(individual_block):

    files_positions = {}
    free_spaces_positions = {}
    free_space_id = 0
    idx = 0

    while idx < len(individual_block):

        # File
        if individual_block[idx] != '.':
            cur_file_id = individual_block[idx]
            starting_position = idx
            pointer = 0
            while pointer < len(individual_block[idx:]) and idx+pointer+1<len(individual_block) and individual_block[idx + pointer + 1] == cur_file_id:
                pointer += 1
                if idx + pointer + 1 > len(individual_block):
                    break
            ending_position = idx + pointer
            files_positions[individual_block[idx]] = [starting_position, ending_position]
            idx = ending_position+1

        # Free space
        else:
            starting_position = idx
            pointer = 0
            while pointer < len(individual_block[idx:]) and idx+pointer+1<len(individual_block) and individual_block[idx + pointer + 1] == '.':
                pointer += 1
            ending_position = idx + pointer
            free_spaces_positions[free_space_id] = [starting_position, ending_position]
            free_space_id += 1
            idx = ending_position+1

    return files_positions, free_spaces_positions


def organize_dict_order(data):
    
    filtered_data = {k: v for k, v in data.items() if v[0] >= 0}

    # Step 2: Sort by the first element in the values
    sorted_data = sorted(filtered_data.values(), key=lambda x: x[0])

    # Step 3: Merge consecutive ranges
    merged_data = []
    current_range = sorted_data[0]

    for i in range(1, len(sorted_data)):
        if sorted_data[i][0] <= current_range[1] + 1:  # Consecutive or overlapping
            current_range[1] = max(current_range[1], sorted_data[i][1])
        else:
            merged_data.append(current_range)
            current_range = sorted_data[i]
    merged_data.append(current_range)  # Add the last range

    # Step 4: Reassign keys based on order
    result = {i + 1: v for i, v in enumerate(merged_data)}

    return result


def move_files_to_free_spaces(files_positions, free_spaces_positions):
    
    for file_id in reversed(files_positions):
        if file_id == 0:
            break
        original_sapce_id = len(free_spaces_positions)
        free_space_id = 0
        # 9: (40, 41)
        # print("\nfile id: ", file_id, "\noriginal files positions[file_id]: ", files_positions[file_id])
        file_length = files_positions[file_id][1] - files_positions[file_id][0] + 1
        leftmosted_free_space_length = free_spaces_positions[free_space_id][1] - free_spaces_positions[free_space_id][0] + 1
        # print("file_length: ", file_length)

        # Find if three is a free space that is big enough for the file movement
        while free_space_id < len(free_spaces_positions):
            leftmosted_free_space_length = free_spaces_positions[free_space_id][1] - free_spaces_positions[free_space_id][0] + 1
            if file_length <= leftmosted_free_space_length and files_positions[file_id][1] > free_spaces_positions[free_space_id][1]:
                # print("leftmosted_free_space_length: ", leftmosted_free_space_length)
                original_file_position = files_positions[file_id]
                files_positions[file_id] = [free_spaces_positions[free_space_id][0], free_spaces_positions[free_space_id][0] + file_length - 1]
                # Update the free space starting position if there is still free space left
                if file_length < leftmosted_free_space_length:
                    free_spaces_positions[free_space_id][0] = free_spaces_positions[free_space_id][0] + file_length
                # Otherwise, remove the free space
                else:
                    free_spaces_positions[free_space_id] = [-10, -100]
                # When the file is moved to the free space, the original file space becomes a free space
                if original_file_position not in free_spaces_positions.values():
                    free_spaces_positions[original_sapce_id] = original_file_position
                original_sapce_id += 1
                # print("New file position: ", files_positions[file_id])    
                break
            free_space_id += 1

        # print("new free space positions: ", free_spaces_positions)
    # free_spaces_positions = organize_dict_order(free_spaces_positions)
    return files_positions, free_spaces_positions


def calculate_checksum_part2(files_positions):

    print("files_positions for calculating the checksum: ", files_positions)

    checksum = 0
    for file_id in files_positions:
        for i in range(files_positions[file_id][0], files_positions[file_id][1]+1):
            # print("i: ", i)
            checksum += file_id * i

    return checksum


if __name__ == "__main__":
    
    input_file = "input.txt"
    input_content = read_input(input_file)

    # Part 1
    # individual_block = convert_str_to_block(input_content)
    # print("individual_block before moving: ", individual_block, "\n")
    # individual_block = move_file_blocks(individual_block)
    # # print("individual_block after moving: ", individual_block)
    # checksum = cal_filesystem_checksum(individual_block)
    # print("Part 1 the checksum is ", checksum)

    # Part 2
    individual_block = convert_str_to_block(input_content)
    # print("individual_block before moving: ", individual_block, "\n")
    # print("the length of the individual_block before moving: ", len(individual_block), "\n")
    files_positions, free_spaces_positions = identify_files_and_free_space(individual_block)
    # print("files_positions: ", files_positions)
    # print("free_spaces_positions: ", free_spaces_positions)
    moved_files_positions, moved_free_spaces_positions = move_files_to_free_spaces(files_positions, free_spaces_positions)
    # print("moved_files_positions: ", moved_files_positions, "\nmoved_free_spaces_positions: ", moved_free_spaces_positions)
    checksum = calculate_checksum_part2(moved_files_positions)
    print("Part 2 the checksum is ", checksum)