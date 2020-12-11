import time

def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    
    content = [int(x.strip()) for x in content]
    return content

def main(filename):

    content = read_file(filename)
    
    for n in content:
        x = abs(n - 2020)
        if x in content:
            return n*x


def main2(filename):

    content = read_file(filename)
    m = {}

    for n in content:
        x = abs(n - 2020)
        m[n] = x

    for key, value in m.items():
        if value in m:
            return value * key

def main3(filename):

    content = read_file(filename)
    content.sort()
    for n in content:
        x = abs(n - 2020)
        if bin_search(content, x) != -1:
            return n*x
        
def bin_search(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        step = step+1
        mid = (start + end) / 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    return -1

if __name__ == "__main__":
    t0 = time.time()
    n = main("input-1.txt")
    t1 = time.time()
    print (n, (t1-t0))

    t0 = time.time()
    n = main2("input-1.txt")
    t1 = time.time()
    print (n, (t1-t0))

    t0 = time.time()
    n = main3("input-1.txt")
    t1 = time.time()
    print (n, (t1-t0))