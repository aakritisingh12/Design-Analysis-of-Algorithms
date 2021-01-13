def extract(Q, w):
    m = 0
    minimum = w[0]
    for i in range(len(w)):
        if w[i] < minimum:
            minimum = w[i]
            m = i
    return m, Q[m]


def dijkstra(Graph, s):
    Q = [s]
    p = {s: None}
    w = [0]
    d = {}
    for i in G:
        d[i] = float('inf')
        Q.append(i)
        w.append(d[i])
    d[s] = 0
    S = []
    n = len(Q)
    while Q:
        u = extract(Q, w)[1]
        S.append(u)
        Q.remove(u)
        for v in Graph[u]:
            if d[v] >= d[u] + Graph[u][v]:
                d[v] = d[u] + Graph[u][v]
                p[v] = u
    return d, p


G = {
    "a": {"b": 4, "h": 8},
    "b": {"a": 4, "c": 8, "h": 11},
    "c": {"b": 8, "d": 7, "f": 14, "i": 2},
    "d": {"c": 7, "e": 6, "f": 14},
    "e": {"d": 6, "f": 10},
    "f": {"c": 4, "d": 14, "e": 10, "g": 2},
    "g": {"f": 2, "h": 1, "i": 6},
    "h": {"a": 8, "b": 11, "g": 1, "i": 7},
    'i': {'c': 2, 'g': 6, 'h': 7}
}

print("Shortest distance from vertex a")
print("Vertex \t\t\tDistance from Source a")

dict = dijkstra(G, "a")[0]
for i in dict:
    print(i, "\t\t\t\t\t\t", dict[i])
