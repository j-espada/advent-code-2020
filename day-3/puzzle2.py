from puzzle1 import tree_count_for_slope
from puzzle1 import read_file

def multiple_tree_slope(lst_splope, map_basis):
    acc = 1
    for slope in lst_splope:
        acc *= tree_count_for_slope(slope[0], slope[1], map_basis)
    return acc

if __name__ == "__main__":
    map_basis = read_file("input-3.txt")
    lst_splope = {(1,1), (3,1), (5,1), (7,1), (1,2)}
    print(multiple_tree_slope(lst_splope, map_basis))
