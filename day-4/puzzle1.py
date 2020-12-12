import re

'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID) -> might miss
'''
def readfile(filename):
    with open(filename) as f:
        return f.readlines()

def pre_process(passports):
    f = lambda x: "{0}:[0-9]([^\s]+)|\n".format(x)
    m = {}
    passports_lst = {}

    for passline in passports:
        if "\n" == passline:
            m = {}
        else:
           pid = 

def main(filename):

    content = readfile(filename)
    pre_process(content)

if __name__ == "__main__":
    main("input-4.txt")