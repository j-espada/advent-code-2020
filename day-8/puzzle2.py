from puzzle1 import Node
from puzzle1 import read_file
from puzzle1 import has_cycle
from puzzle1 import apply_statement
from puzzle1 import NOP, ACC, JMP
import numpy as np

def check_cycle(progam, statement, new_instruction):

    old_value = statement.instruction

    statement.instruction = new_instruction
    acc, is_cycle, _pred, _statement = has_cycle(progam)
    statement.instruction = old_value

    return acc, is_cycle, _pred, _statement

def brute_force(filename):
    orginal_program = read_file("input-8.txt")
    return find_acc(orginal_program, orginal_program)

def find_acc(program, statements):
    for statement in statements:
        acc = None
        is_cycle = None
        if statement.is_operation(JMP):
            acc, is_cycle, _pred, _statement = check_cycle(program, statement, NOP)
        elif statement.is_operation(NOP):
            acc, is_cycle, _pred, _statement = check_cycle(program, statement, JMP)
        if is_cycle is False:
            return acc

def enum_cycle(statement, program, pred):
    id = statement.id
    cycle = set()
    while id != None and program[id] not in cycle:
        cycle.add(program[id])
        id = pred[id]
    return cycle

def from_cycle(filename):
    orginal_program = read_file(filename)
    _acc, is_cycle, pred, statement = has_cycle(orginal_program)
    
    if is_cycle:
        cycle = enum_cycle(statement, orginal_program, pred)
        #print("brute force: ", len(list(filter(lambda x: x.instruction in {JMP, NOP}, orginal_program))))
        #print("cycle: ", len(list(filter(lambda x: x.instruction in {JMP, NOP}, cycle))))
        return find_acc(orginal_program, cycle)

if __name__ == "__main__":
    print(from_cycle("input-8.txt"))