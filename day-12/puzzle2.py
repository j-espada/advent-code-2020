from puzzle1 import read_file
from puzzle1 import taxi_cab_dist
import numpy as np


ROTATION_MATRIXES = {
    90 : np.array([[0, -1], [1, 0]]), 
    180 : np.array([[-1, 0], [0, -1]]), 
    270 : np.array([[0, 1], [-1, 0]])
}

def rotate(point, center, deg):
    _point = np.array(point)
    _center = np.array(center)
    delta = _point - _center
    return np.matmul(ROTATION_MATRIXES[deg], delta) + _center

def main(file_name):
    instructions =  read_file(file_name)

    # north/south ; west/east
    boat = [0, 0]
    waypoint = [1, 10]

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
            waypoint = rotate(waypoint, boat, value % 360)
        elif action == 'R':
            waypoint =rotate(waypoint, boat, (360 - value))
         
        elif action == 'F':
           
            boat[0] += value * waypoint[0]
            boat[1] += value * waypoint[1]

            waypoint[0] +=  boat[0]
            waypoint[1] +=  boat[1]

        print(action, value)
        print("waypoint : ", waypoint)
        print("boat : ", boat)



if __name__ == "__main__":
    main("test.txt")
