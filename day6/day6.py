import sys
sys.path.insert(0, "../")
from general import *


def determine_starting_position(grid):

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == '^':
                return i, j


def calculate_guard_route(grid):

    row = len(grid)
    column = len(grid[0])
    
    i, j = determine_starting_position(grid)

    while (grid[i][j]=='^' and i!=0) or (grid[i][j]=='>' and j!=column-1) or (grid[i][j]=='v' and i!=row-1) or (grid[i][j]=='<' and j!=0):

        """move up"""
        if grid[i][j] == '^':
            # Check if there's a row above
            while i > 0:
                if grid[i-1][j] != '#':
                    grid[i-1][j] = grid[i][j]
                    grid[i][j] = 'X'
                else:
                    grid[i][j] = '>'
                    break
                i = i - 1
        """move right"""
        if grid[i][j] == '>':
            # Check if there's a column on the right
            while j < column-1:
                if grid[i][j+1] != '#':
                    grid[i][j+1] = grid[i][j]
                    grid[i][j] = 'X'
                else:
                    grid[i][j] = 'v'
                    break
                j = j + 1
        """move down"""
        if grid[i][j] == 'v':
            # if there's a row below
            while i < row-1:
                if grid[i+1][j] != '#':
                    grid[i+1][j] = grid[i][j]
                    grid[i][j] = 'X'
                else:
                    grid[i][j] = '<'
                    break
                i = i + 1
        """move left"""
        if grid[i][j] == '<':
            # if there's a column on the left
            while j > 0:
                if grid[i][j-1] != '#':
                    grid[i][j-1] = grid[i][j]
                    grid[i][j] = 'X'
                else:
                    grid[i][j] = '^'
                    break
                j = j - 1

    return grid


def count_X(grid):

    count = 1

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 'X':
                count += 1

    return count


def calculate_guard_route_with_obstruction(grid, i, j):

    row = len(grid)
    column = len(grid[0])
    visited_states = set()

    while (grid[i][j]=='^' and i!=0) or (grid[i][j]=='>' and j!=column-1) or (grid[i][j]=='v' and i!=row-1) or (grid[i][j]=='<' and j!=0):

        grid_state = tuple(tuple(row) for row in grid)
        if grid_state in visited_states:
            print("Dead loop detected!")
            return True
        visited_states.add(grid_state)

        """move up"""
        if grid[i][j] == '^':
            # Check if there's a row above
            while i > 0:
                if (grid[i-1][j] != '#') and (grid[i-1][j] != 'O'):
                    grid[i-1][j] = grid[i][j]
                    grid[i][j] = 'X'
                else:
                    grid[i][j] = '>'
                    break
                i = i - 1
        """move right"""
        if grid[i][j] == '>':
            # Check if there's a column on the right
            while j < column-1:
                if (grid[i][j+1] != '#') and (grid[i][j+1] != 'O'):
                    grid[i][j+1] = grid[i][j]
                    grid[i][j] = 'X'
                else:
                    grid[i][j] = 'v'
                    break
                j = j + 1
        """move down"""
        if grid[i][j] == 'v':
            # if there's a row below
            while i < row-1:
                if (grid[i+1][j] != '#') and (grid[i+1][j] != 'O'):
                    grid[i+1][j] = grid[i][j]
                    grid[i][j] = 'X'
                else:
                    grid[i][j] = '<'
                    break
                i = i + 1
        """move left"""
        if grid[i][j] == '<':
            # if there's a column on the left
            while j > 0:
                if (grid[i][j-1] != '#') and ((grid[i][j-1] != 'O')):
                    grid[i][j-1] = grid[i][j]
                    grid[i][j] = 'X'
                else:
                    grid[i][j] = '^'
                    break
                j = j - 1

    return False


def set_obstruction(input_content):

    option = 0

    grid = input_content.strip().splitlines()
    grid = [list(row) for row in grid]
    starting_i, starting_j = determine_starting_position(grid)

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if (i == starting_i) and (j == starting_j):
                continue
            grid = input_content.strip().splitlines()
            grid = [list(row) for row in grid]
            grid[i][j] = 'O'
            if calculate_guard_route_with_obstruction(grid, starting_i, starting_j):
                option += 1
    
    return option


if __name__ == "__main__":
    
    input_file = "input.txt"
    input_content = read_input(input_file)
    grid = input_content.strip().splitlines()
    grid = [list(row) for row in grid]

    routed_grid = calculate_guard_route(grid)
    result_part1 = count_X(routed_grid)
    print("The result of part 1: ", result_part1)
    
    result_part2 = set_obstruction(input_content)
    print("The result of part 2: ", result_part2)