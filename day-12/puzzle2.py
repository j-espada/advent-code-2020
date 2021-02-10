from puzzle1 import read_file
from puzzle1 import taxi_cab_dist
import numpy as np
import math

def rotate(point, origin, angle):
    # source: https://stackoverflow.com/a/34374437
    ox, oy = origin
    px, py = point
    _angle = np.radians(angle)
    qx = ox + np.cos(_angle) * (px - ox) - np.sin(_angle) * (py - oy)
    qy = oy + np.sin(_angle) * (px - ox) + np.cos(_angle) * (py - oy)
    return np.array([int(round(qx)), int(round(qy))])

def main(file_name):
    instructions =  read_file(file_name)

    # north/south ; west/east
    boat = np.array([0, 0])
    waypoint = np.array([10, 1])

    for action, value in instructions:
        if action == 'N':
            waypoint[1] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'W':
            waypoint[0] -= value
        elif action == 'L':
            waypoint = rotate(waypoint, (0,0), value)
        elif action == 'R':
            waypoint = rotate(waypoint, (0,0), (-value)) 
        elif action == 'F':  
            boat[0] += waypoint[0] * value
            boat[1] += waypoint[1] * value
        
        print(action, value)
        print("waypoint : ", waypoint)
        print("boat : ", boat)
    
    print("taxi cab: ", taxi_cab_dist(boat, [0,0]))

if __name__ == "__main__":
    main("input-12.txt")
