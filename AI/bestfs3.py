import heapq
import networkx as nx
import matplotlib.pyplot as plt

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    parent = {start: None}

    while pq:
        cost, current_node = heapq.heappop(pq)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]

        if current_node not in visited:
            visited.add(current_node)
            for neighbour in graph[current_node]:
                if neighbour not in visited:
                    parent[neighbour] = current_node
                    heapq.heappush(pq, (heuristic[neighbour], neighbour))

    return None

# Graph definition
Graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}

# Run the search
path = best_first_search(Graph, 'A', 'F', heuristic)
print("Best First Search Path:", path)

# Visualize the graph
G = nx.Graph()
for node, neighbors in Graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500,
        font_size=12, font_weight='bold')
if path:
    nx.draw_networkx_edges(G, pos,
        edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)],
        edge_color='red', width=2)
plt.title("Graph Visualization with Best First Search Path")
plt.show()
