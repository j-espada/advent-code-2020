def parse_info(info):
    y = info.split()
    letter = str(y[1][0])
    passwd = str(y[2]).strip()
    p = y[0].find('-')
    min_times = int(str(y[0])[0:p])
    max_times = int(str(y[0])[p+1::])
    return (letter, passwd, min_times, max_times)

def is_valid(x):
    letter, passwd, min_times, max_times = parse_info(x)
    m = {letter:0}
    for y in passwd:
        if y in m:
            m[y] = m[y] + 1
        else:
            m[y] = 0
    return min_times <= m[letter] <= max_times

def main(filename, valid_func):
    content = read_file(filename)
    valid_lst = filter(lambda x: valid_func(x), content)
    return len(valid_lst)

def read_file(filename):
     with open(filename) as f:
        content = f.readlines()
        return content
    
if __name__ == "__main__":
    n = main("input-2.txt", is_valid)
    print (n)
