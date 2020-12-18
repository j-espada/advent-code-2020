from puzzle1 import Node
from puzzle1 import read_file
from puzzle1 import has_cycle
from copy import deepcopy

def check_cycle(progam, i, new_instruction):

    old_value = progam[i].instruction
    progam[i].instruction = new_instruction
    acc, is_cycle = has_cycle(progam)
    progam[i].instruction = old_value

    return acc, is_cycle

def main(filename):

    orginal_program = read_file("input-8.txt")

    for i in range(len(orginal_program)):
        acc = None
        is_cycle = None
        if orginal_program[i].is_operation("jmp"):
            acc, is_cycle = check_cycle(orginal_program,i, "nop")
        elif orginal_program[i].is_operation("nop"):
            acc, is_cycle = check_cycle(orginal_program,i, "nop")

        if is_cycle is False:
            return acc

if __name__ == "__main__":
    print(main("input-8.txt"))