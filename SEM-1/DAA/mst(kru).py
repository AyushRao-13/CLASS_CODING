class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(n, edges):
    edges.sort()  
    dsu = DisjointSet(n)


    mst_weight = 0
    mst_edges = []

    for w, u, v in edges:
        if dsu.find(u) != dsu.find(v):  
            dsu.union(u, v)
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges


if __name__ == "__main__":
    edges = [
        (10, 0, 1),
        (6, 0, 2),
        (5, 0, 3),
        (15, 1, 3),
        (4, 2, 3)
    ]
    mst_weight, mst_edges = kruskal(4, edges)

    print("Edges in MST:", mst_edges)
    print("Total weight of MST:", mst_weight)
