def dijkstra(graph, origin, destiny):
    distances = {node: float('inf') for node in graph.content}
    distances[origin] = 0

    visited = []

    shortest_paths = {}

    while len(visited) != len(graph.content):
        current_node = None
        current_distance = float('inf')
        for node in graph.content:
            if distances[node] < current_distance and node not in visited:
                current_node = node
                current_distance = distances[node]

        if current_node is None:
            break

        if current_node not in visited:
            visited.append(current_node)

        for neighbor, weight in graph[current_node]:
            distance = int(current_distance) + int(weight)
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_paths[neighbor] = current_node

    if distances[destiny] == float('inf'):
        return None

    path = []
    node = destiny
    while node != origin:
        path.append(node)
        node = shortest_paths[node]
    path.append(origin)
    path.reverse()

    return path, distances[destiny]


def run(graph, origin, destiny, runner):
    if runner:
        print("\n\nDijkstra:\n---------------------")
        path, weight = dijkstra(graph, origin, destiny)
        if path:
            return path, weight
        else:
            print("No path found.")
            return None, None

    # CHECK: IF RETURNS COST
