from puzzle1 import read_file
from puzzle1 import taxi_cab_dist
import numpy as np


ROTATION_MATRIXES = {90 : np.array([[], []]), 180: np.array([[], []]), 270: np.array([[], []])}

def rotate(point, center, deg):

    _point = np.array(point)
    _center = np.array(point)
    _deg = deg
    print(deg, _deg)
    delta = _point - _center
    rot = np.array([
        [int(np.cos(_deg)), int(-np.sin(_deg))], 
        [int(np.sin(_deg)), int(np.cos(_deg))]
                    ])
    print(rot)
    return rot * delta + _center

def main(file_name):
    instructions =  read_file(file_name)

    # north/south ; west/east
    boat = [0, 0]
    waypoint = [boat[0] + 1, boat[1] + 10]

    for action, value in instructions:
        
        if action == 'N':
            waypoint[0] += value
        elif action == 'S':
            waypoint[0] += value
        elif action == 'E':
            waypoint[1] += value
        elif action == 'W':
            waypoint[1] -= value
        elif action == 'L':
            pass
        elif action == 'R':
            print(rotate(waypoint, boat, 90))
            print(rotate(waypoint, boat, 180))
            print(rotate(waypoint, boat, 270))

        elif action == 'F':
            boat[0] += value * waypoint[0]
            boat[1] += value * waypoint[1]

        print(action, value)
        print("waypoint : ", waypoint)
        print("boat : ", boat)



if __name__ == "__main__":
    main("test.txt")
