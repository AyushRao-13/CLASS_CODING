import matplotlib.pyplot as plt
import networkx as nx

def hill_climbing(graph, heuristic, start, goal):
    path = [start]
    current = start
    while current != goal:
        neighbors = graph[current]
        if not neighbors:
            print("No path found")
            return path
        next_node = min(neighbors, key=lambda x: heuristic[x])
        if heuristic[next_node] >= heuristic[current]:
            print("Local optimum reached or dead end.")
            break
        path.append(next_node)
        current = next_node
    return path

# Define graph and heuristics
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'G'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
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

# Run hill climbing
solution_path = hill_climbing(graph, heuristic, 'A', 'G')
print("Solution Path:", solution_path)

# Visualization
def visualize_graph(graph, heuristic, path):
    G = nx.DiGraph()

    # Add nodes and edges
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)  # consistent layout

    # Node colors — highlight the path
    node_colors = []
    for node in G.nodes():
        if node in path:
            node_colors.append("lightgreen")
        else:
            node_colors.append("lightcoral")

    # Draw nodes, edges, and labels
    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=node_colors,
        node_size=1500,
        font_size=12,
        font_weight="bold",
        arrows=True,
        arrowstyle="->",
        arrowsize=20
    )

    # Add heuristic values as node labels
    labels = {n: f"{n}\n(h={heuristic[n]})" for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_color="black")

    # Highlight the path edges in blue
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="blue", width=2.5)

    plt.title("Hill Climbing Algorithm Visualization", fontsize=14)
    plt.show()

# Call visualization function
visualize_graph(graph, heuristic, solution_path)
