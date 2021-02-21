from functools import reduce

def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
        line = [x.strip() for x in content][1]
        line = [x for x in line.split(',')]
        l = []
        for i in range(len(line)):
            bus_id = line[i]
            if bus_id != 'x':
                l.append((int(bus_id), i))
        return l

if __name__ == "__main__":
    lst_bus = read_file("test.txt")

    m = {}
    
    for b in lst_bus:
        bus, _delta = b
        m[bus] = set()

    counter = 0

    while True:
        for b in lst_bus:
            bus, delta = b
            m[bus].add((counter * bus) + delta)

        x = reduce((lambda x,y: x&y), m.values())

        if(len(x) > 0):
            print(x)

            print(m)
            break

     

        counter += 1

        
