import heapq
def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

graph = {
'P': [('Q', 4), ('R', 2), ('F', 9)],
'Q': [('P', 4), ('R', 5), ('S', 10)],
'R': [('P', 2), ('Q', 5), ('S', 3), ('E', 4)],
'S': [('Q', 10), ('R', 3), ('E', 1)],
'E': [('R', 4), ('S', 1)],
'F': [('P', 9)]
}
start_node = 'P'
distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, ":")
for node, d in distances.items():
    print(f"{start_node} → {node} = {d}")