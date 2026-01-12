import heapq
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, heuristic, path=None):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, cost in neighbors:
            G.add_edge(node, neighbor, weight=cost)

    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=False, node_size=700, node_color="lightblue", font_weight="bold")

    labels = {node: f"{node}({heuristic[node]})" for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight="bold")

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2.5)

    plt.title("A* Search Path with Heuristics")
    plt.show()

def a_star_search(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))
    came_from = {}

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    closed_set = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        closed_set.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]

                if not any(neighbor == item[1] for item in open_set):
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 1), ('E', 4)],
    'C': [('A', 3), ('F', 2)],
    'D': [('B', 1)],
    'E': [('B', 4), ('F', 1)],
    'F': [('C', 2), ('E', 1)]
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0  # Goal
}

visualize_graph(graph, heuristic)

path = a_star_search(graph, 'B', 'F', heuristic)  
print("A* search path:", path)

visualize_graph(graph, heuristic, path)
