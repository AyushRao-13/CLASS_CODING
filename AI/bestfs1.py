import heapq
import networkx as nx
import matplotlib.pyplot as plt

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in parent:
                parent[neighbour] = current
                heapq.heappush(pq, (heuristic[neighbour], neighbour))

    return None


# Graph definition
Graph = {
    'X': ['Y', 'A', 'H'],
    'Y': ['X', 'A', 'M', 'Z'],
    'Z': ['Y', 'N'],
    'A': ['X', 'Y', 'M'],
    'M': ['Y', 'A', 'P'],
    'N': ['Z', 'P'],
    'H': ['X', 'O', 'R'],
    'O': ['H', 'R'],
    'P': ['M', 'N', 'R', 'S'],
    'R': ['H', 'O', 'P', 'T', 'K'],
    'S': ['P', 'K'],
    'T': ['R', 'K', 'V'],
    'V': ['T', 'K'],
    'K': ['R', 'T', 'V', 'S']
}

# Heuristic values
heuristic = {
    'X': 5,
    'Y': 10,
    'Z': 13,
    'A': 4,
    'M': 6,
    'N': 9,
    'H': 6,
    'O': 7,
    'R': 3,
    'P': 8,
    'S': 4,
    'T': 7,
    'V': 4,
    'K': 0
}

# Run Best First Search
path = best_first_search(Graph, 'X', 'K', heuristic)
print("Best First Search Path:", path)

# Visualization
G = nx.Graph()
for node, neighbors in Graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

pos = nx.spring_layout(G, seed=42)

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10)

if path:
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

plt.title("Best First Search Path from 'X' to 'K'")
plt.show()
