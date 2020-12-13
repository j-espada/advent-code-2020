from puzzle1 import pre_process
from puzzle1 import readfile
import re

def valid_byr(passport):
    byr = passport['byr']
    return 1920 <= int(byr) <= 2002

def valid_iyr(passport):
    iyr = passport['iyr']
    return 2010 <= int(iyr) <= 2020

def valid_eyr(passport):
    eyr = passport['eyr']
    return 2020 <= int(eyr) <= 2030

def valid_hgt(passport):
    hgt = passport['hgt']
    if "cm" in hgt:
        hgt = hgt.replace("cm", "")
        return 150 <= int(hgt) <= 193
    elif "in" in hgt:
        hgt = hgt.replace("in", "")
        return 59 <= int(hgt) <= 76
    else:
        return False

def valid_hcl(passport):
    return re.match(r'^#[0-9a-f]{6}$', passport['hcl'])

def valid_ecl(passport):
    return passport['ecl'] in {'amb', 'blu', 'brn','gry','grn','hzl','oth'}

def valid_pid(passport):
    return len(passport['pid']) == 9 and passport['pid'].isdigit()

def is_valid(passport):

    required_entries = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    for f in required_entries:
        if(f not in passport):
            return False

    return valid_byr(passport) and valid_iyr(passport) and valid_eyr(passport) and valid_hgt(passport) and\
         valid_ecl(passport) and valid_hcl(passport) and valid_pid(passport)

def main(filename):

    data = readfile(filename)
    passports = pre_process(data)
    acc = 0

    for passport in passports:
        if is_valid(passport):
            acc += 1

    return acc

if __name__ == "__main__":
    print(main("input-4.txt"))

