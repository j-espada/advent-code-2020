from puzzle1 import read_file
from puzzle1 import bin_search

def main(filename):

    content = read_file(filename)
    
    for x in content: 
       for y in content:
        if x == y:
            continue
        for z in content:
            if x == z and y == z:
                continue
            if x + z + y == 2020:
                return x*z*y

def main2(filename):
    content = read_file(filename)
    content.sort()
    for x in content: 
        for y in content:
            if x == y:
                continue
            z = x + y
            if z <= 2020:
                w = 2020 - z               
                if bin_search(content, w) != -1:
                    return w*x*y

def main3(filename):
    content = read_file(filename)
    m = {}
    for x in content: 
        for y in content:
            if x == y:
                continue
            z = x + y
            if z <= 2020:
                w = 2020 - z 
                m[w] = (x,y)              
    for n in content:
        if n in m:
            x,y = m[n]
            return n * x * y
    

if __name__ == "__main__":
    n = main("input-1.txt")
    print (n)
    
    n = main2("input-1.txt")
    print (n)

    n = main3("input-1.txt")
    print (n)