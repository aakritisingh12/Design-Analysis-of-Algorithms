parent = dict()
rank = dict()


def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0


def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
        minimum_spanning_tree = set()
        # edges = list(graph['edges'])
        graph['edges'].sort()
    # print edges
    for edge in graph['edges']:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)


graph = {
    'vertices': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
    'edges': [
        (8, 'a', 'h'),
        (4, 'a', 'b'),
        (4, 'b', 'a'),
        (8, 'b', 'c'),
        (11, 'b', 'h'),
        (8, 'c', 'b'),
        (2, 'c', 'i'),
        (4, 'c', 'f'),
        (7, 'c', 'd'),
        (7, 'd', 'c'),
        (14, 'd', 'f'),
        (6, 'd', 'e'),
        (6, 'e', 'd'),
        (10, 'e', 'f'),
        (10, 'f', 'e'),
        (14, 'f', 'd'),
        (4, 'f', 'c'),
        (2, 'f', 'g'),
        (2, 'g', 'f'),
        (6, 'g', 'i'),
        (1, 'g', 'h'),
        (1, 'h', 'g'),
        (7, 'h', 'i'),
        (11, 'h', 'b'),
        (8, 'h', 'a'),
        (7, 'i', 'h'),
        (2, 'i', 'c'),
        (6, 'i', 'g')
    ]
}

result = kruskal(graph)
for i in result:
    print(i)
