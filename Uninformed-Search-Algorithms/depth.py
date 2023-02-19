def depth_first_search(graph, origin, destiny, path=None):
    if path is None:
        path = []

    path.append(origin)

    if origin == destiny:
        return path

    for neighbor in graph.content[origin]:
        neighbor = neighbor[0]
        if neighbor not in path:
            new_path = depth_first_search(graph, neighbor, destiny, path.copy())
            if new_path is not None:
                return new_path
    return None


def run(graph, origin, destiny, runner):
    if runner:
        print("\n\nDepth First Search:\n---------------------")
        path = depth_first_search(graph, origin, destiny)
        if path:
            return path
        else:
            print("No path found.")
            return None
