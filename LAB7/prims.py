from sys import maxsize

INF = maxsize
V = 9


def isValidEdge(u, v, inMST):
    if u == v:
        return False
    if inMST[u] is False and inMST[v] is False:
        return False
    elif inMST[u] is True and inMST[v] is True:
        return False
    return True


def primMST(Graph):
    inMST = [False] * V

    inMST[0] = True

    edge_count = 0
    mincost = 0
    while edge_count < V - 1:

        minn = INF
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if Graph[i][j] < minn:
                    if isValidEdge(i, j, inMST):
                        minn = Graph[i][j]
                        a = i
                        b = j

        if a != -1 and b != -1:
            print('({}, {}, {})'.format(dict[a], dict[b], minn))
            edge_count += 1
            mincost += minn
            inMST[b] = inMST[a] = True

    print("Minimum cost = %d" % mincost)


dict = {0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h',
        8: 'i'}

Graph = [[INF, 4, INF, INF, INF, INF, INF, 8, INF],
         [4, INF, 8, INF, INF, INF, INF, 11, INF],
         [INF, 8, INF, 7, INF, 4, INF, INF, 2],
         [INF, INF, 7, INF, 6, 14, INF, INF, INF],
         [INF, INF, INF, 6, INF, 10, INF, INF, INF],
         [INF, INF, 4, 14, 10, INF, 2, INF, INF, ],
         [INF, INF, INF, INF, INF, 2, INF, 1, 6],
         [8, 11, INF, INF, INF, INF, 1, INF, 7],
         [INF, INF, 2, INF, INF, 6, INF, 7, INF]]

primMST(Graph)
