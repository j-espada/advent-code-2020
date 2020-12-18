import numpy as np

JMP = "jmp"
NOP = "nop"
ACC = "acc"
class Node:

    def __init__(self, instruction, id):
        s = instruction.split(" ")
        self.instruction = s[0]
        self.quantity = int(s[1])
        self.id = int(id)

    def is_operation(self, op):
        return op == self.instruction

    def __str__(self):
        return "instruction: " + self.instruction \
        + " id: " + str(self.id) \
        + " quantity: " + str(self.quantity)
    
    def __repr__(self):
        return self.__str__()

def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    
    r = []
    for i in range(len(content)):
        r.append(Node(content[i].strip(), i))

    return r

def main(filename):
    progam = read_file(filename)
    return has_cycle(progam)
   
def has_cycle(progam):
    acc = 0
    statement_pointer = 0
    last_pointer = len(progam) - 1
    visited = np.full(len(progam), False)
    pred = np.full(len(progam), -1)
    while True:

        statement = progam[statement_pointer]

        if visited[statement.id]:
            return (acc, True, pred, statement)
        
        if last_pointer == statement_pointer:
            statement_pointer, acc = apply_statement(statement, statement_pointer, acc, visited, pred)
            return (acc, False, pred, statement)

        statement_pointer, acc = apply_statement(statement, statement_pointer, acc, visited, pred)

def apply_statement(statement, statement_pointer, acc, visited, pred):

    old_st_pointer = statement_pointer

    if statement.is_operation(NOP):
        statement_pointer+=1
    elif statement.is_operation(ACC):
        acc += statement.quantity
        statement_pointer+=1
    elif statement.is_operation(JMP):
        statement_pointer += statement.quantity
    
    visited[statement.id] = True
    pred[old_st_pointer] = statement_pointer

    return statement_pointer, acc

if __name__ == "__main__":
    print(main("input-8.txt")[0])