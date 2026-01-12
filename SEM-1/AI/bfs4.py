from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def breadth_first_search_visualized(graph, start_node):
    visited= set()
    queue= deque([start_node])
    visited.add(start_node)

    G=nx.DiGraph(graph)

    pos= nx.spring_layout(G)

    visited_nodes=set()
    visited_edges=set()

    while queue:
        vertex = queue.popleft()
        visited_nodes.add(vertex)

        node_colors = ['red' if node not in visited_nodes else 'green' for node in G.nodes()]
        edge_colors= ['black' if edge not in visited_edges else 'blue' for edge in G.edges()]

        plt.figure(figsize=(8,6))
        nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=3000, font_size=18, font_weight='bold', arrowsize=20)
        plt.show()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                visited_edges.add((vertex, neighbor))

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A','G'],
        'C': ['A','B'],
        'D': ['A','E','F'],
        'E': ['D','F','H'],
        'F': ['D','E','H','I'],
        'G': ['B','F','J'],
        'H': ['E','F','I'],
        'I': ['A','E','F'],
        'J': ['G','K'],
        'K': ['J','I']
    }

    print("Breadth First Search Visualization Starting From Vertex 'E':")
    breadth_first_search_visualized(graph, 'E')
