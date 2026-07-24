from itertools import permutations

LIMIT = float("inf")


def simplify_matrix(matrix):

    updated = [row[:] for row in matrix]

    length = len(updated)
    total_reduction = 0

    for r in range(length):

        minimum = min(updated[r])

        if minimum != 0 and minimum != LIMIT:

            total_reduction += minimum

            updated[r] = [
                value - minimum if value != LIMIT else LIMIT
                for value in updated[r]
            ]

    for c in range(length):

        minimum = min(updated[r][c] for r in range(length))

        if minimum != 0 and minimum != LIMIT:

            total_reduction += minimum

            for r in range(length):

                if updated[r][c] != LIMIT:
                    updated[r][c] -= minimum

    return updated, total_reduction


def shortest_tour(graph, vertices):

    remaining_nodes = list(range(1, vertices))

    best_distance = LIMIT
    best_route = []

    for order in permutations(remaining_nodes):

        current_route = [0] + list(order) + [0]

        distance = sum(
            graph[current_route[i]][current_route[i + 1]]
            for i in range(vertices)
        )

        if distance < best_distance:
            best_distance = distance
            best_route = current_route

    return best_route, best_distance


travel_cost = [
    [LIMIT, 11, 15, 9, 13],
    [11, LIMIT, 14, 8, 7],
    [15, 14, LIMIT, 12, 10],
    [9, 8, 12, LIMIT, 6],
    [13, 7, 10, 6, LIMIT]
]

locations = ["X", "Y", "Z", "W", "V"]

total_places = len(travel_cost)

route, minimum_cost = shortest_tour(travel_cost, total_places)

print("Travelling Salesman Cost Matrix\n")

print(f'{"":>5}', end="")
for place in locations:
    print(f"{place:>6}", end="")
print()

for index, values in enumerate(travel_cost):

    print(f"{locations[index]:>5}", end="")

    for value in values:

        if value == LIMIT:
            print(f'{"INF":>6}', end="")
        else:
            print(f"{value:>6}", end="")

    print()

print("\nBest Route:")
print(" -> ".join(locations[i] for i in route))

print("\nMinimum Distance:", minimum_cost)

print("\nTravel Details:")

for i in range(total_places):

    start = route[i]
    end = route[i + 1]

    print(f"{locations[start]} -> {locations[end]} : {travel_cost[start][end]}")
