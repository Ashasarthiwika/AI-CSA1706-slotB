import heapq

graph = {
    "A": {"B": 1, "C": 3},
    "B": {"D": 3, "E": 1},
    "C": {"F": 2},
    "D": {"G": 2},
    "E": {"G": 2},
    "F": {"G": 1},
    "G": {}
}

heuristic = {
    "A": 6,
    "B": 4,
    "C": 4,
    "D": 2,
    "E": 2,
    "F": 1,
    "G": 0
}

def a_star(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for neighbour, distance in graph[node].items():
            new_cost = cost + distance
            new_f = new_cost + heuristic[neighbour]

            heapq.heappush(
                queue,
                (new_f, new_cost, neighbour, path + [neighbour])
            )

    return None, None


path, cost = a_star("A", "G")

print("Best Path:", path)
print("Cost:", cost)
