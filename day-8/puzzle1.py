import numpy as np
class Node:

    def __init__(self, instruction, id):
        s = instruction.split(" ")
        self.instruction = s[0]
        self.quantity = int(s[1])
        self.id = id

    def is_operation(self, op):
        return op in self.instruction

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
    visited = np.zeros(len(progam))

    while True:

        statement = progam[statement_pointer]

        if visited[statement.id]:
            return (acc, True)
        
        if last_pointer == statement_pointer:
            statement, statement_pointer, acc, visited = apply_statement(statement, statement_pointer, acc, visited)
            return (acc, False)

        statement, statement_pointer, acc, visited = apply_statement(statement, statement_pointer, acc, visited)

def apply_statement(line, statement_pointer, acc, visited):

    if line.is_operation("nop"):
        statement_pointer+=1
    elif line.is_operation("acc"):
        acc += line.quantity
        statement_pointer+=1
    elif line.is_operation("jmp"):
        statement_pointer += line.quantity
    
    visited[line.id] = True
    return line, statement_pointer, acc,visited

if __name__ == "__main__":
    # sol 1384
    print(main("input-8.txt"))