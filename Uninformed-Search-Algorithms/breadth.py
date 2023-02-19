def breadth_first_search(graph, origin, destiny):
    queue = [[origin]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == destiny:
            return path
        for adjacent in graph.content[node]:
            new_path = list(path)
            new_path.append(adjacent[0])
            queue.append(new_path)
    return None


def run(graph, origin, destiny, runner):
    if runner:
        print("\n\nBreadth First Search:\n---------------------")
        path = breadth_first_search(graph, origin, destiny)
        if path:
            return path
        else:
            print("No path found.")
            return None
