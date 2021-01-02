PREAMBLE_SIZE = 25
START_POSITION = 26

def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    return content

def not_in_preamble(preamble, n):
    b = False
    for k in preamble:
        for j in preamble:
            if k == j: 
                continue
            if (k+j) == n:
                b = True
    return not b

def main(filename):
    c = read_file(filename)
    for i in range(START_POSITION, len(c), 1):        
        b = not_in_preamble(c[i-PREAMBLE_SIZE-1:i], c[i])
        if b:
            return c[i]

if __name__ == "__main__":
    print(main("input-9.txt"))