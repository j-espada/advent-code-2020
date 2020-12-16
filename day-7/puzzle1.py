def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content]
    return content

def build_graph(content):

    remove_digits = lambda x: str(filter(lambda c: not c.isdigit(), x))
    G = {}
    for line in content:
        edge = line.split("contain")
        node = remove_digits(edge[0])
        node = node.replace('bags','')
        node = node.replace('bag','')
        node = node.strip(' ')
    
        neighbors = edge[1].split(",")

        if node not in G:
            G[node] = []
        
        for n in neighbors:
            _n = remove_digits(n)
            _n = _n.replace('bags','')
            _n = _n.replace('bag','')
            _n = _n.replace('.','')
            _n = _n.strip(' ')
            G[node].append(_n)

            if _n not in G:
                G[_n] = []
    
    return G


def bfs(G, source, dest):

    Q = [source] # queue
    V = set() # visited

    while len(Q) > 0:
        p = Q.pop(0)

        # avoid cycle structures
        if p in V:
            continue

        if p == dest:
            return True
        
        for n in G[p]:
            Q.append(n)
    
    return False

def main(filename):

    content = read_file(filename)
    G = build_graph(content)

    dst = "shiny gold"
    acc = 0
    for n in G:
        if n != dst:
            if bfs(G, n, dst):
                acc += 1

    return acc

if __name__ == "__main__":
    filename = "input-7.txt"
    print(main(filename))