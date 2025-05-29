"""

Union find simple implementation

contains two functions
one is find that finds which set it belongs to
union merges two blocks if they are connected through current node



"""

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot != yroot:
        return False
    parent[yroot] = xroot
    return True


def has_cycle(edges, n):
    parent = list(range(n))
    for u, v in edges:
        if not union(parent, u, v):
            return True
    
    return False

# Needs adjecency list as input
# edges = [(0, 1), (1,2), (2,0)]

# Should try more examples on this union and find this kind of merges two sets based on which cycle they belong to
# Helps in finfding the cycles within the graphs
