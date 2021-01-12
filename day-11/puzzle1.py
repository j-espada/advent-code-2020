EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
FLOOR = '.'
DIRECTIONS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
        content = [list(x.strip()) for x in content]
        return content

def iter(max_row, max_col):
    for i in range(max_row):
        for j in range(max_col):
            yield (i,j)

def print_grid(grid):
    for r in range(len(grid)):
        print(grid[r])

def count_occupied (r, c, max_row, max_col, grid):
    count = 0 
    # 8 neighoring position
    for i,j in DIRECTIONS:
        delta_r = r + i
        delta_c = c + j
        if 0 <= delta_r < max_row and 0 <= delta_c < max_col and grid[delta_r][delta_c] == OCCUPIED_SEAT:
            count += 1
    return count

def main(file_name, count_occupied_seats, occ_seats=4):
    grid = read_file(file_name)
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    while True:
        update = []
        
        for r,c in iter(n_rows, n_cols):
            k = grid[r][c]
            count_occ = count_occupied_seats(r, c, n_rows, n_cols, grid)
            if k == EMPTY_SEAT and count_occ == 0:
                update.append((r, c, OCCUPIED_SEAT))
            elif k == OCCUPIED_SEAT and count_occ >= occ_seats:    
                update.append((r, c, EMPTY_SEAT))
                             
        for r,c,s in update:
            grid[r][c] = s

        if len(update) == 0:
            break
        
    n = sum(map(lambda x: x.count(OCCUPIED_SEAT), grid))
    print(n)

if __name__ == "__main__":
    file_name = "input-11.txt"
    main(file_name, count_occupied)
