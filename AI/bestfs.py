import heapq
import networkx as nx
import matplotlib.pyplot as plt

def best_first_search(graph,start,goal,heuristic):
  visited = set()
  pq = []
  heapq.heappush(pq,(heuristic[start],start))
  parent = {start:None}

  while pq:
    current_h, current = heapq.heappop(pq)

    if current == goal:
      path = []
      while parent[current] is not None:
        path.append(current)
        current = parent[current]
      path.append(start) # Add the start node to the path
      return path[::-1]

    visited.add(current)
    for neighbor in graph[current]:
      if neighbor not in visited:
        parent[neighbor] = current
        heapq.heappush(pq,(heuristic[neighbor],neighbor))
  return None # Return None if goal is not reached


graph = {
      'X' : ['Q', 'M', 'Y'],
      'Y' : ['X', 'Z'],
      'Z' : ['N', 'Y'],
      'L' : ['M', 'Y'],
      'M' : ['L', 'X', 'P'],
      'N' : ['P', 'Z', 'U'],
      'O' : ['Q', 'P'],
      'P' : ['R', 'S', 'M', 'N', 'O'],
      'Q' : ['X', 'O', 'R', 'V'],
      'R' : ['P', 'Q', 'T'],
      'S' : ['V', 'P'],
      'T' : ['R', 'U'],
      'U' : ['T', 'N', 'V'],
      'V' : ['Q', 'S', 'U']
}

heuristic = {
      'X' : 5,
      'Y' : 10,
      'Z' : 13,
      'L' : 4,
      'M' : 6,
      'N' : 9,
      'O' : 7,
      'P' : 8,
      'Q' : 6,
      'R' : 3,
      'S' : 4,
      'T' : 7,
      'U' : 5,
      'V' : 8
}

odd_path = best_first_search(graph,'X','U',heuristic)
even_path = best_first_search(graph,'Z','U',heuristic)
print('Best First Search path for odd start'+ str(odd_path))
print('Best First Search path for even start'+ str(even_path))

# Create a graph object
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(graph.keys())

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Define positions for the nodes (you can adjust these for better visualization)
pos = nx.spring_layout(G)  # or nx.kamada_kawai_layout(G) or nx.circular_layout(G) etc.

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')

# Highlight the paths
if odd_path:
    odd_path_edges = list(zip(odd_path, odd_path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=odd_path, node_color='red', node_size=800)
    nx.draw_networkx_edges(G, pos, edgelist=odd_path_edges, edge_color='red', width=2)

if even_path:
    even_path_edges = list(zip(even_path, even_path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=even_path, node_color='lightgreen', node_size=800)
    nx.draw_networkx_edges(G, pos, edgelist=even_path_edges, edge_color='lightgreen', width=2)


# Display the plot
plt.title("Graph Visualization with Best First Search Paths")
plt.show()