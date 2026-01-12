def hill_climbing(graph, heuristic, start, goal):
    path=[start]
    current = start
    while current != goal:
        neighbors = graph[current]
        if not neighbors:
            print("no path found")
            return path
        next_node = min(neighbors, key=lambda x:heuristic[x])
        if heuristic[next_node] >= heuristic[current]:
            print("Local optimum reached or dead end.")
            break
        path.append(next_node)
        current= next_node
    return path

graph= {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F':['G'],
    'G':[]
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 1,
    'G': 0
}

solution_path= hill_climbing(graph, heuristic, 'A', 'G')
print ("solution Path:", solution_path)
