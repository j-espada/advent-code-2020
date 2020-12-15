from puzzle1 import readfile

def main(filename):

    asnwers = readfile(filename)
    answer_count = {}
    lst = []
    n_voters = 0
    for answer in asnwers:
        if answer == "":
            lst.append((n_voters, answer_count))
            answer_count = {}
            n_voters = 0
        else:
            for char in answer:
                if char in answer_count:
                    answer_count[char] += 1
                else:
                    answer_count[char] = 1
            n_voters+=1

    counter = 0

    for s, answer_count in lst:  
        for _k, v in answer_count.items():
            if v == s:
                counter = counter + 1
    
    return counter
        
if __name__ == "__main__":
    print(main("input-6.txt"))