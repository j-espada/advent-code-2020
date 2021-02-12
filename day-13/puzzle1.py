TIME_STAMP = "timestamp"
BUS = "bus"

def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
        lines = [x.strip() for x in content]
        bus_map = {
            TIME_STAMP : int(lines[0]), 
            BUS : list(map(lambda y: int(y) , filter(lambda x: x != 'x' , [x for x in lines[1].split(',')])))
        }
        return bus_map

def main(file_name):
    bus_map = read_file(file_name)

    timestamp = bus_map[TIME_STAMP]
    bus_lst = bus_map[BUS]
    bus_time_stamp_map = {}

    for bus in bus_lst:
        times = [x for x in range(0, timestamp + bus + 1, bus)]
        times = list(filter(lambda x: x >= timestamp, times))
        bus_time_stamp_map[bus] = times

    bus_id, min_val = min(bus_time_stamp_map.items(), key=lambda x: x[1]) 
    print((min_val[0] - timestamp) * bus_id)

if __name__ == "__main__":
    main("input-13.txt")
        
