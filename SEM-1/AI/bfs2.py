from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

G = nx.DiGraph(graph)
pos = nx.spring_layout(G)

nx.draw(G,pos,with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold', arrowsize=20)

plt.show()

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

        node_colors = ['skyblue' if node not in visited_nodes else 'yellow' for node in G.nodes()]
        edge_colors= ['black' if edge not in visited_edges else 'red' for edge in G.edges()]

        plt.figure(figsize=(8,6))
        nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=2000, font_size=16, font_weight='bold', arrowsize=20)
        plt.show()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                visited_edges.add((vertex, neighbor))

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("Breadth First Search Visualization Starting From Vertex 'A':")
    breadth_first_search_visualized(graph, 'A')    


