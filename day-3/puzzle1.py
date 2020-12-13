from itertools import chain, tee

tree = "#"

def read_file(filename):
        board = []
        with open(filename) as f:
            rows = f.readlines()
            for row in rows:
                tmp = []
                row = row.strip()
                for col in row:
                    tmp.append(col)
                board.append(tmp)
        return board

def is_tree(x, y, board):
    map_x = x % len(board[y])
    return board[y][map_x] == tree

def tree_count(right_increment, down_increment, board):
    # initial position is (0,0)
    right_coordinate = 0
    down_coordinate = 0
    tree_count = 0
    
    # go down until the end of the map
    while down_coordinate < len(board):
        if is_tree(right_coordinate, down_coordinate, board):
            tree_count += 1
        right_coordinate += right_increment
        down_coordinate += down_increment
 
    return tree_count
    
if __name__ == "__main__":
    board = read_file("input-3.txt")
    print("Number of trees: ", tree_count(3, 1, board))