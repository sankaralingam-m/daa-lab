import heapq


class DisjointSet:

    def __init__(self, vertices):
        self.root = list(range(vertices))
        self.depth = [0] * vertices

    def find_root(self, node):
        if self.root[node] != node:
            self.root[node] = self.find_root(self.root[node])
        return self.root[node]

    def merge(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)

        if root1 == root2:
            return False

        if self.depth[root1] < self.depth[root2]:
            root1, root2 = root2, root1

        self.root[root2] = root1

        if self.depth[root1] == self.depth[root2]:
            self.depth[root1] += 1

        return True


def kruskal_mst(vertices, edge_list):

    sorted_edges = sorted(edge_list)

    ds = DisjointSet(vertices)

    mst_edges = []
    total_weight = 0

    for weight, source, destination in sorted_edges:

        if ds.merge(source, destination):
            mst_edges.append((source, destination, weight))
            total_weight += weight

        if len(mst_edges) == vertices - 1:
            break

    return mst_edges, total_weight


def prim_mst(vertices, graph, start_vertex=0):

    minimum = float("inf")

    distance = [minimum] * vertices
    previous = [-1] * vertices
    visited = [False] * vertices

    distance[start_vertex] = 0

    priority_queue = [(0, start_vertex)]

    mst_edges = []
    total_weight = 0

    while priority_queue:

        current_weight, current_vertex = heapq.heappop(priority_queue)

        if visited[current_vertex]:
            continue

        visited[current_vertex] = True

        if previous[current_vertex] != -1:
            mst_edges.append(
                (previous[current_vertex], current_vertex, current_weight)
            )
            total_weight += current_weight

        for neighbour, edge_weight in graph.get(current_vertex, []):

            if not visited[neighbour] and edge_weight < distance[neighbour]:
                distance[neighbour] = edge_weight
                previous[neighbour] = current_vertex
                heapq.heappush(priority_queue, (edge_weight, neighbour))

    return mst_edges, total_weight


number_of_vertices = 5

edges = [
    (2, 0, 1),
    (6, 0, 3),
    (3, 1, 2),
    (8, 1, 3),
    (5, 1, 4),
    (7, 2, 4),
    (9, 3, 4)
]

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

kruskal_result, kruskal_cost = kruskal_mst(number_of_vertices, edges)
prim_result, prim_cost = prim_mst(number_of_vertices, graph)

print("Kruskal's MST")
print("Edges :", kruskal_result)
print("Cost  :", kruskal_cost)

print("\nPrim's MST")
print("Edges :", prim_result)
print("Cost  :", prim_cost)