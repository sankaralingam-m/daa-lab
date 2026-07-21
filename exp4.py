import heapq


def shortest_path(network, start):

    total_nodes = len(network)

    minimum_distance = [float("inf")] * total_nodes
    previous_node = [None] * total_nodes

    minimum_distance[start] = 0

    priority_queue = [(0, start)]
    explored = set()

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in explored:
            continue

        explored.add(current_node)

        for next_node, edge_cost in network[current_node]:

            if minimum_distance[current_node] + edge_cost < minimum_distance[next_node]:

                minimum_distance[next_node] = minimum_distance[current_node] + edge_cost
                previous_node[next_node] = current_node

                heapq.heappush(
                    priority_queue,
                    (minimum_distance[next_node], next_node)
                )

    return minimum_distance, previous_node


def trace_path(previous_node, start, destination):

    route = []
    current = destination

    while current is not None:
        route.append(current)
        current = previous_node[current]

    route.reverse()

    if route and route[0] == start:
        return route

    return []


network = {
    0: [(1, 3), (2, 6)],
    1: [(2, 2), (3, 5)],
    2: [(3, 1), (4, 4)],
    3: [(5, 2)],
    4: [(5, 3)],
    5: []
}

start_vertex = 0

distance, previous = shortest_path(network, start_vertex)

print(f"Shortest Distance from Vertex {start_vertex}\n")

print(f'{"Node":<8}{"Distance":<12}{"Shortest Path"}')
print("-" * 45)

for node in range(len(network)):

    route = trace_path(previous, start_vertex, node)

    if route:
        route_text = " -> ".join(map(str, route))
    else:
        route_text = "Not Reachable"

    value = distance[node] if distance[node] != float("inf") else "INF"

    print(f"{node:<8}{value!s:<12}{route_text}")