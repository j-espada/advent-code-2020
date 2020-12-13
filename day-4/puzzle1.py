def readfile(filename):
    with open(filename) as file:
        data = [line.strip() for line in file]
        data.append("")
        return data

def pre_process(data):
   
    passports = [] 
    passport = {}

    for line in data:
        if line == "":
            passports.append(passport)
            passport = {}
        else:
            fields = line.split()
            for field in fields:
                field = field.split(":")
                passport[field[0]] = field[1]
    
    return passports

def main(filename):

    data = readfile(filename)
    passports = pre_process(data)
    acc = 0

    required_entries = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    for passport in passports:
        if all(val in passport for val in required_entries):
            acc += 1

    print(acc)

if __name__ == "__main__":
    main("input-4.txt")