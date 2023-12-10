
from collections import deque
def add_edge(node1, node2):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)

def create_edges(raw):
    current_node = (0, 0)
    for input_string in raw:
        for char in input_string:
            if char == '-':
                add_edge(current_node, (current_node[0], current_node[1] + 1))
                add_edge(current_node, (current_node[0], current_node[1] - 1))
            elif char == '|':
                add_edge(current_node, (current_node[0] + 1, current_node[1]))
                add_edge(current_node, (current_node[0] - 1, current_node[1]))
            elif char == '7':
                add_edge(current_node, (current_node[0], current_node[1] - 1))
                add_edge(current_node, (current_node[0] + 1, current_node[1]))
            elif char == 'J':
                add_edge(current_node, (current_node[0], current_node[1] - 1))
                add_edge(current_node, (current_node[0] - 1, current_node[1]))
            elif char == 'L':
                add_edge(current_node, (current_node[0], current_node[1] + 1))
                add_edge(current_node, (current_node[0] - 1, current_node[1]))
            elif char == 'F':
                add_edge(current_node, (current_node[0], current_node[1] + 1))
                add_edge(current_node, (current_node[0] + 1, current_node[1]))
            elif char == 'S':
                #hard
                add_edge(current_node, (current_node[0], current_node[1] - 1))
                add_edge(current_node, (current_node[0] + 1, current_node[1]))
                starting = current_node
            current_node = (current_node[0], current_node[1] +1) if current_node else (0, 0)
        current_node = (current_node[0]+1,0)
    return starting

def soln(graph):
    #Part 1
    visited = set()
    queue = deque([(starting, 0)])  # Tuple (node, distance)
    furthest_node = None
    while queue:
        current_node, distance = queue.popleft()
        furthest_node = current_node

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if current_node in graph[neighbor]: #reciprocity
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))
    #Part 2
    current_node = (0, 0)
    ym = len(l)
    xm = len(l[0])-1
    ins = 0
    while current_node[0] < ym:
        bars = 0
        dashes = 0
        while current_node[1] < xm:
            if current_node in visited:
                #print(current_node)
                c = graph[current_node]
                tiletype = (c[0][0]-c[1][0],c[0][1]-c[1][1])
                #(-1 1) F   
                #(1 -1) J
                #(1 1) L
                #(-1 -1) 7
                if tiletype == (2,0):
                    bars = not bars
                if tiletype == (1,1):
                    dashes = 1
                if tiletype == (-1,1):
                    dashes = 2
                if tiletype == (-1,-1):
                    if dashes == 1:
                        dashes = 0
                        bars = not bars
                    if dashes == 2:
                        dashes = 0
                if tiletype == (1,-1):
                    if dashes == 1:
                        dashes = 0
                    if dashes == 2:
                        dashes = 0
                        bars = not bars
            else:
                ins += bars
            current_node = (current_node[0],current_node[1]+1)
        current_node = (current_node[0]+1, 0)
    return furthest_node, distance,ins

folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'
l=[]

graph= {}
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):        
        l.append(line)
starting = create_edges(l)

print(soln(graph))

