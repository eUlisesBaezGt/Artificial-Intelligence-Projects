from queue import PriorityQueue


def BranchAndBound(graph, origin, destination):
    visited = set()
    frontier = PriorityQueue()
    # Tuple contains the current path cost, current node, and the path so far
    frontier.put((0, origin, [origin]))
    while not frontier.empty():
        cost, node, path = frontier.get()
        if node == destination:
            print(f"Cost: {cost}")
            return path
        visited.add(node)
        for neighbor, weight in graph.nodes[node].items():
            if neighbor not in visited:
                new_path = path + [neighbor]
                bound = cost + int(weight)
                frontier.put((bound, neighbor, new_path))
    return None
