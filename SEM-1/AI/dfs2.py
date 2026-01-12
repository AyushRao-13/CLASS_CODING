import networkx as nx
import matplotlib.pyplot as plt

graph ={
    'A': ['B','G'],
    'B': ['A','C','E'],
    'C': ['B','D'],
    'D': ['C','J','I'],
    'E': ['B','F','I'],
    'F': ['G','E'],
    'G': ['A','F','H','L'],
    'H': ['G','I'],
    'I':['D','E','H','K'],
    'J':['D','M','N'],
    'K':['I','L','M'],
    'L':['G','K','M','O'],
    'M':['L','K','J'],
    'N':['J','O'],
    'O':['N','L']
}

G = nx.Graph(graph)
pos = nx.spring_layout(G)

nx.draw(G,pos,with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold')

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
    
start_node = 'O'
depth_first_search(graph, start_node)