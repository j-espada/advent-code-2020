from puzzle1 import main
from puzzle1 import OCCUPIED_SEAT, EMPTY_SEAT, DIRECTIONS

def occupied(r, c, max_row, max_col, grid):
    counter = 0

    for i,j in DIRECTIONS:
        delta_r, delta_c =r + i, c + j

        while 0 <= delta_r < max_row and 0 <= delta_c < max_col:
            if grid[delta_r][delta_c] == OCCUPIED_SEAT:
                counter += 1
                break

            elif grid[delta_r][delta_c] == EMPTY_SEAT:
                break
            delta_r += i
            delta_c += j
    return counter

if __name__ == "__main__":
    file_name = "input-11.txt"
    main(file_name, occupied, 5)