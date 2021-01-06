def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    return content

def main(file_name):
    c = read_file(file_name)
    c.append(0)
    c.append(max(c) + 3)
    c.sort()
    diff_map = {1: 0, 2: 0, 3:0}
    for i in range(len(c) - 1):
        j = i + 1
        diff = c[j] - c[i]
        diff_map[diff] += 1 
    
    print("1: {0}, 3: {1}".format(diff_map[1], diff_map[3]))
    print("result: ", diff_map[1]*diff_map[3])
    
if __name__ == "__main__":
    main("input-10m p.txt")