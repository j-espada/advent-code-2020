def read_file(filename):
        matrix = []
        with open(filename) as f:
            rows = f.readlines()
            for row in rows:
                tmp = []
                row = row.strip()
                for col in row:
                    tmp.append(col)
                print(len(tmp))
                matrix.append(tmp)
        return matrix

def is_tree_at_coordinates(hill_x, hill_y, map_basis):
    map_x = hill_x % len(map_basis[hill_y])
    return map_basis[hill_y][map_x] == "#"

def tree_count_for_slope(right_increment, down_increment, map_basis):
    right_coordinate = 0
    down_coordinate = 0
    tree_count = 0
 
    while down_coordinate < len(map_basis):
        if is_tree_at_coordinates(right_coordinate, down_coordinate, map_basis):
            tree_count += 1
        right_coordinate += right_increment
        down_coordinate += down_increment
 
    return tree_count
    
if __name__ == "__main__":
    map_basis = read_file("input-3.txt")
    print(tree_count_for_slope(3,1, map_basis))



  

