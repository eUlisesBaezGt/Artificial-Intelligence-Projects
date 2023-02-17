import functions as f

def dijkstra(graph, origin, destiny):
    distances = {node: float('inf') for node in graph}
    distances[origin] = 0

    visited = []

    shortest_paths = {}

    while len(visited) != len(graph):
        current_node = None
        current_distance = float('inf')
        for node in graph:
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


def run(graph):
    print("\n\nDijkstra's algorithm:\n---------------------")
    print("Origin: ", end="")
    origin = input()
    print("Destiny: ", end="")
    destiny = input()
    path = dijkstra(graph, origin, destiny)
    f.show_path(path, origin, destiny)
