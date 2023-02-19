import iterative_depth as id


def two_way_search(graph, origin, destiny):
    path = id.iterative_depth(graph, origin, destiny)
    if path:
        return path
    else:
        path = id.iterative_depth(graph, destiny, origin)
        if path:
            path.reverse()
            return path
        else:
            return None


def run(graph, origin, destiny, runner):
    if runner:
        print("\n\nTwo Way Search:\n--------------")
        path = two_way_search(graph, origin, destiny)
        if path:
            return path
        else:
            print("No path found.")
            return None
