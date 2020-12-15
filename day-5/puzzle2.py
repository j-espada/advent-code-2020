from puzzle1 import read_file
from puzzle1 import get_seat
from puzzle1 import to_id

from puzzle1 import n_rows, n_cols

import numpy as np
import sys

def main(filename):

    tickets = read_file(filename)
    seats = [get_seat(x) for x in tickets]
    plain = np.zeros((n_rows, n_cols))

    for s in seats:
        r,c = s
        plain[r][c] = 1

    in_bounds = lambda x,y: 0 <= x < n_rows and 0 <= y < n_cols

    for i in range(n_rows):
        for j in range(n_cols):

            if plain[i][j] != 0:
                continue

            res = True
            for k in range(-1,2,1):
                for w in range(-1,2,1):
                    if (k,w) != (0,0) and in_bounds(i+k,j+w) and plain[i+k][j+w] == 0:
                        res = False
            
            if res is True:
                return to_id(i,j)


if __name__ == "__main__":
    np.set_printoptions(threshold=sys.maxsize)
    print(main("input-5.txt"))