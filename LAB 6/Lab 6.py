graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4, 5],
    4: [2, 3],
    5: [3, 6],
    6: [5]
}

dict_keys = [key for key in graph]

graph2 = {1: [2], 2: [3], 3: [4], 4: [4]}


def bfs(graph, initial):
    visited = []

    queue = [initial]

    while queue:

        node = queue.pop(0)
        if node not in visited:

            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return visited


print("Graph traversal using BFS: ", bfs(graph, 1))


def dfs(graph, initial):
    visited = []

    stack = [initial]

    while stack:

        node = stack.pop(-1)
        if node not in visited:

            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                stack.append(neighbour)
    return visited


# DFS using adjecency list

# graph = {1: [2, 3], 2: [1, 4], 3: [1, 4, 5], 4: [2, 3], 5: [3, 6], 6: [5]}
dict_keys = [key for key in graph]


def strongly_connected(graph, start):
    visited = []
    stack = [start]

    while len(stack) != 0:
        current = stack.pop()
        if current not in visited:
            visited.append(current)

            for neighbours in graph[current]:
                stack.append(neighbours)

    # checking if a graph is strongly connected or not
    if visited != graph.keys():
        print("This Graph is strongly connected")

    else:
        print("This graph is not strongly connected")

    return visited


print("Graph traversal using DFS: ", dfs(graph, dict_keys[0]))
# DFS using adjecency list

graph = {1: [2, 3], 2: [1, 4], 3: [1, 4, 5], 4: [2, 3], 5: [3], 6: []}
dict_keys = [key for key in graph]

strongly_connected(graph, 1)

numtime = {}
for i in dict_keys:
    numtime.update({i: [0, 0]})


def pre_and_post(graph):
    global numtime

    time = 0
    dict_keys_2 = [key for key in graph]

    for node in graph:
        time += 1
        if len(graph[node]) != 0:
            numtime[node][0] = time
        else:

            numtime[node][0] = time
            time += 1
            numtime[node][1] = time
            count = dict_keys_2.index(node)
            while count >= 0:
                numtime[dict_keys_2[count]][1] = time
                time += 1
                count -= 1

            return numtime


nuber = (pre_and_post(graph))
for i in range(len(nuber)):
    print(i+1, ":", nuber[i+1])