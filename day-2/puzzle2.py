from puzzle1 import main
from puzzle1 import parse_info

def is_valid(x):
    letter, passwd, p1, p2 = parse_info(x)
    if (passwd[p1 - 1] == letter and passwd[p2 - 1] != letter) or (passwd[p1 - 1] != letter and passwd[p2 - 1] == letter):
        return True
    else:
        return False

if __name__ == "__main__":
    n = main("input-2.txt", is_valid)
    print (n)