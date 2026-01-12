import networkx as nx
import matplotlib.pyplot as plt

graph ={
    'A': ['B','C','D'],
    'B': ['D','E'],
    'C': ['F'],
    'D': ['E'],
    'E': ['F'],
    'F': []
}

G = nx.DiGraph(graph)
pos = nx.spring_layout(G)

nx.draw(G,pos,with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold', arrowsize=20)

plt.show()

def depth_first_search(graph, start_node):
    visited = set()
    
    def dfs(node):
        visited.add(node)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)
    
    dfs(start_node)
    
start_node = 'A'
depth_first_search(graph, start_node)