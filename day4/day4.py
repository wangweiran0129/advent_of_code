import sys
sys.path.insert(0, "../")
from general import *


def match_xmas(input_content):

    count = 0
    grid = input_content.strip().splitlines()
    row = len(grid)
    column = len(grid[0])

    for r in range(row):
        for c in range(column):
            # Horizontal XMAS
            if (c+3<column) and (grid[r][c]=='X') and (grid[r][c+1]=='M') and (grid[r][c+2]=='A') and (grid[r][c+3]=='S'):
                count += 1
            # Horizontal SAMX
            if (c+3<column) and (grid[r][c]=='S') and (grid[r][c+1]=='A') and (grid[r][c+2]=='M') and (grid[r][c+3]=='X'):
                count += 1
            # Vertical XMAS
            if (r+3<row) and (grid[r][c]=='X') and (grid[r+1][c]=='M') and (grid[r+2][c]=='A') and (grid[r+3][c]=='S'):
                count += 1
            # Vertical SAMX
            if (r+3<row) and (grid[r][c]=='S') and (grid[r+1][c]=='A') and (grid[r+2][c]=='M') and (grid[r+3][c]=='X'):
                count += 1
            # Diagnoal XMAS
            if (c+3<column) and (r+3<row) and (grid[r][c]=='X') and (grid[r+1][c+1]=='M') and (grid[r+2][c+2]=='A') and (grid[r+3][c+3]=='S'):
                count += 1
            # Anti-Diagnoal XMAS
            if (c+3<column) and (r+3<row) and (grid[r][c+3]=='X') and (grid[r+1][c+2]=='M') and (grid[r+2][c+1]=='A') and (grid[r+3][c]=='S'):
                count += 1
            # Diagnoal SAMX
            if (c+3<column) and (r+3<row) and (grid[r][c]=='S') and (grid[r+1][c+1]=='A') and (grid[r+2][c+2]=='M') and (grid[r+3][c+3]=='X'):
                count += 1
            # Anti-Diagnoal SAMX
            if (c+3<column) and (r+3<row) and (grid[r][c+3]=='S') and (grid[r+1][c+2]=='A') and (grid[r+2][c+1]=='M') and (grid[r+3][c]=='X'):
                count += 1
    
    return count


def match_x_mas(input_content):

    count = 0
    grid = input_content.strip().splitlines()
    row = len(grid)
    column = len(grid[0])

    for r in range(row):
        for c in range(column):
            """
            M S
             A
            M S
            """
            if (r+2<row) and (c+2<column) and (grid[r][c]=='M') and (grid[r][c+2]=='S') and (grid[r+1][c+1]=='A') and (grid[r+2][c]=='M') and (grid[r+2][c+2]=='S'):
                count += 1
            """
            S M
             A
            S M
            """
            if (r+2<row) and (c+2<column) and (grid[r][c]=='S') and (grid[r][c+2]=='M') and (grid[r+1][c+1]=='A') and (grid[r+2][c]=='S') and (grid[r+2][c+2]=='M'):
                count += 1
            """
            M M
             A
            S S
            """
            if (r+2<row) and (c+2<column) and (grid[r][c]=='M') and (grid[r][c+2]=='M') and (grid[r+1][c+1]=='A') and (grid[r+2][c]=='S') and (grid[r+2][c+2]=='S'):
                count += 1
            """
            S S
             A
            M M
            """
            if (r+2<row) and (c+2<column) and (grid[r][c]=='S') and (grid[r][c+2]=='S') and (grid[r+1][c+1]=='A') and (grid[r+2][c]=='M') and (grid[r+2][c+2]=='M'):
                count += 1
    return count


if __name__ == "__main__":
    
    input_file = "input.txt"
    input_content = read_input(input_file)
    part_1_result = match_xmas(input_content)
    print("The result of part 1 is: ", part_1_result)
    part_2_result = match_x_mas(input_content)
    print("The result of part 2 is: ", part_2_result)
