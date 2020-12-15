def readfile(filename):
    with open(filename) as file:
        data = [line.strip() for line in file]
        data.append("")
        return data

def group_answers(asnwers):

    group = []
    s = set()
    for answer in asnwers:
        
        if answer == "":
            group.append(s)
            s = set()
        else:
            for char in answer:
                s.add(char)
    
    return group

def count_answers(groups):

    acc = 0 
    for check in groups:
        acc += len(check)
    return acc

def main(filename):

    asnwers = readfile("input-6.txt")
    groups = group_answers(asnwers)
    return count_answers(groups)

if __name__ == "__main__":
    print(main("input-6.txt"))
    
