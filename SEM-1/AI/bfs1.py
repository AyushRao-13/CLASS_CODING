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

