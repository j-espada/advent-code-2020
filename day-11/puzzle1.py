EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
FLOOR = '.'

def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
        content = [list(x.strip()) for x in content]
        return content

def iter(max_row, max_col):
    for i in range(max_row):
        for j in range(max_col):
            yield (i,j)

def adj_pos(row, col, max_row, max_col):
    for i in range(-1,2):
        for j in range(-1,2):
            if row == row + i and col == col + j:
                continue
            if 0 <= row + i < max_row and 0 <= col + j < max_col:
                yield (row+i, col+j)

def print_grid(grid):
    for r in range(len(grid)):
        print(grid[r])

def main(file_name, neighbor_pos):
    grid = read_file(file_name)
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    chaos = False
    while True:
        update = []
        for r,c in iter(n_rows, n_cols):
            k = grid[r][c]
            if k == EMPTY_SEAT:
                    adj_occupied = True
                    for _r,_c in neighbor_pos(r, c, n_rows, n_cols):
                        if grid[_r][_c] == OCCUPIED_SEAT:
                            adj_occupied = False
                            break
                    if adj_occupied:
                        update.append((r, c, OCCUPIED_SEAT))
                        chaos = True
            elif k == OCCUPIED_SEAT:
                    counter = 0
                    for _r,_c in neighbor_pos(r, c, n_rows, n_cols):
                        if grid[_r][_c] == OCCUPIED_SEAT:
                            counter += 1
                        if counter >= 4:
                            update.append((r, c, EMPTY_SEAT))
                            chaos = True
                             
        for r,c,s in update:
            grid[r][c] = s

        if chaos == False:
            break

        chaos = False
        
    n = sum(map(lambda x: x.count(OCCUPIED_SEAT), grid))
    print(n)

if __name__ == "__main__":
    file_name = "input-11.txt"
    main(file_name, adj_pos)
