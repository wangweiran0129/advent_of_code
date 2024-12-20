import re
import sys
sys.path.insert(0, "../")
from general import *


def find_antennas_locations(grid, frequencies):

    antennas = {}

    # Antennas frequency is indicated by
    # a single lowercase letter, uppercase letter, or digit
    row = len(grid)
    column = len(grid[0])

    for r in range(0, row):
        for c in range(0, column):
            if grid[r][c] in frequencies:
                antennas.setdefault(grid[r][c], []).append((r, c))

    return antennas


def calculate_antinode_location_4_part_1(grid, antennas):

    # row and column will be the boundary
    row = len(grid)
    column = len(grid[0])
    antinodes_location = []

    for frequency in antennas:
        # antinodes based on the resonant frequencies of the antennas
        if len(antennas[frequency]) > 1:
            # 'a' = [(3, 4), (4, 8), (5, 5)]
            for i in range(0, len(antennas[frequency])-1):
                for j in range(i+1, len(antennas[frequency])):
                    p_1_x, p_1_y = antennas[frequency][i][0], antennas[frequency][i][1]
                    p_2_x, p_2_y = antennas[frequency][j][0], antennas[frequency][j][1]
                    x_diff = p_1_x - p_2_x
                    y_diff = p_1_y - p_2_y
                    if (0<=p_1_x+x_diff<row) and (0<=p_1_y+y_diff<column):
                        antinodes_location.append((p_1_x+x_diff, p_1_y+y_diff))
                    if (0<=p_2_x-x_diff<row) and (0<=p_2_y-y_diff<column):
                        antinodes_location.append((p_2_x-x_diff, p_2_y-y_diff))
    
    return list(set(antinodes_location))


def calculate_antinode_location_4_part_2(grid, antennas):

    # row and column will be the boundary
    row = len(grid)
    column = len(grid[0])
    antinodes_location = []

    for frequency in antennas:
        # antinodes based on the resonant frequencies of the antennas
        if len(antennas[frequency]) > 1:
            # 'T': [(0, 0), (1, 3), (2, 1)]
            for i in range(0, len(antennas[frequency])-1):
                for j in range(i+1, len(antennas[frequency])):
                    p_1_x, p_1_y = antennas[frequency][i][0], antennas[frequency][i][1]
                    p_2_x, p_2_y = antennas[frequency][j][0], antennas[frequency][j][1]
                    x_diff = p_1_x - p_2_x
                    y_diff = p_1_y - p_2_y

                    while (0<=p_1_x+x_diff < row) and (0<=p_1_y+y_diff<column):
                        # print((p_1_x+x_diff, p_1_y+y_diff))
                        antinodes_location.append((p_1_x+x_diff, p_1_y+y_diff))
                        p_1_x = p_1_x+x_diff
                        p_1_y = p_1_y+y_diff
                    while (0<=p_2_x-x_diff<row) and (0<=p_2_y-y_diff<column):
                        # print((p_2_x-x_diff, p_2_y-y_diff))
                        antinodes_location.append((p_2_x-x_diff, p_2_y-y_diff))
                        p_2_x = p_2_x-x_diff
                        p_2_y = p_2_y-y_diff
            antinodes_location.extend(antennas[frequency])
    return list(set(antinodes_location))


if __name__ == "__main__":
    
    input_file = "input.txt"
    input_content = read_input(input_file)
    grid = input_content.strip().splitlines()
    grid = [list(row) for row in grid]

    pattern = r'[a-zA-Z0-9]'
    matches = re.findall(pattern, input_content)
    frequencies = set(matches)
    antennas = find_antennas_locations(grid, frequencies)

    # part 1
    antinodes_location = calculate_antinode_location_4_part_1(grid, antennas)
    print("Part 1 \nHow many unique locations within the bounds of the map contain an antinode: ", len(antinodes_location), "\n")

    # part 2
    antinodes_location_4_part_2 = calculate_antinode_location_4_part_2(grid, antennas)
    # print("antinodes_location_4_part_2: ", antinodes_location_4_part_2)
    print("Part 2 \nHow many unique locations within the bounds of the map contain an antinode: ", len(antinodes_location_4_part_2))