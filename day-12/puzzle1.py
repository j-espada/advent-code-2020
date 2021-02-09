DEGREES_TO_DIR = {0 : 'E', 90: 'N', 180: 'W', 270: 'S'}

def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
        l = []
        for line in content:
            action = line[0]
            value = int(line[1::])
            l.append((action, value))
        return l

def taxi_cab_dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def main(file_name):
    instructions =  read_file(file_name)
    boat = [{'N': 0, 'S': 0, 'E': 0, 'W': 0}, 0]

    for action, value in instructions:
        print(action, value)
        if action in ['N', 'S', 'E', 'W']:
            boat[0][action] += value 
        elif action == 'L':
            boat[1] = boat[1] + value
        elif action == 'R':
            boat[1] = boat[1] + (360 - value)
        elif action == 'F':
            action = DEGREES_TO_DIR[boat[1]%360]
            boat[0][action] += value 
        
        print(boat)
    
    print(taxi_cab_dist((0,0), (boat[0]['N'] -  boat[0]['S'], boat[0]['E'] -  boat[0]['W'])))

if __name__ == "__main__":
    main("input-12.txt")

