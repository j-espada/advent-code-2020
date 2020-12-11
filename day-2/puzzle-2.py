def is_valid(x):
    y = x.split()
    letter = str(y[1][0])
    passwd = str(y[2]).strip()
    p = y[0].find('-')
    min_times = int(str(y[0])[0:p])
    max_times = int(str(y[0])[p+1::])

    m = {letter:0}
    for y in passwd:
        if y in m:
            m[y] = m[y] + 1
        else:
            m[y] = 0
    print(min_times, max_times, passwd, letter, m)
    return min_times <= m[letter] <= max_times

def main(filename):

    with open(filename) as f:
        content = f.readlines()
    
    valid_lst = filter(lambda x: is_valid(x), content)
    return len(valid_lst)

    
if __name__ == "__main__":
    n = main("input-2.txt")
    print (n)
