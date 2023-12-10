
from collections import deque
def add_edge(node1, node2):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)

def create_edges(raw):
    c = (0, 0)
    for input_string in raw:
        for char in input_string:
            if char == '-':
                add_edge(c, (c[0], c[1] + 1))
                add_edge(c, (c[0], c[1] - 1))
            elif char == '|':
                add_edge(c, (c[0] + 1, c[1]))
                add_edge(c, (c[0] - 1, c[1]))
            elif char == '7':
                add_edge(c, (c[0], c[1] - 1))
                add_edge(c, (c[0] + 1, c[1]))
            elif char == 'J':
                add_edge(c, (c[0], c[1] - 1))
                add_edge(c, (c[0] - 1, c[1]))
            elif char == 'L':
                add_edge(c, (c[0], c[1] + 1))
                add_edge(c, (c[0] - 1, c[1]))
            elif char == 'F':
                add_edge(c, (c[0], c[1] + 1))
                add_edge(c, (c[0] + 1, c[1]))
            elif char == 'S':
                #hard
                add_edge(c, (c[0], c[1] - 1))
                add_edge(c, (c[0] + 1, c[1]))
                S = c
            c = (c[0], c[1] +1) if c else (0, 0)
        c = (c[0]+1,0)
    return S

def soln(graph):
    #Part 1
    visited = set()
    queue = deque([(S, 0)])  # Tuple (node, distance)
    furthest_node = None
    while queue:
        c, distance = queue.popleft()
        furthest_node = c

        if c not in visited:
            visited.add(c)
            for neighbor in graph[c]:
                if c in graph[neighbor]: #reciprocity
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))
    #Part 2
    c = (0, 0)
    ym = len(l)
    xm = len(l[0])-1
    ins = 0
    while c[0] < ym:
        pipe = 0
        dash = 0
        while c[1] < xm:
            if c in visited:
                nb = graph[c]
                tiletype = (nb[0][0]-nb[1][0],nb[0][1]-nb[1][1])            
                if tiletype == (2,0): pipe = not pipe
                if tiletype == (1,1): dash = 1 #(1 1) L
                if tiletype == (-1,1): dash = 2 #(-1 1) F   
                if tiletype == (-1,-1): #(-1 -1) 7
                    if dash == 1: dash = 0; pipe = not pipe
                    if dash == 2: dash = 0
                if tiletype == (1,-1): #(1 -1) J
                    if dash == 1: dash = 0
                    if dash == 2: dash = 0; pipe = not pipe
            else:
                ins += pipe
            c = (c[0],c[1]+1)
        c = (c[0]+1, 0)
    return furthest_node, distance,ins

folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'
l=[]

graph= {}
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):        
        l.append(line)
S = create_edges(l)

print(soln(graph))

