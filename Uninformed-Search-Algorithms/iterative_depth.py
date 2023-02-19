import limited_depth as ld


def iterative_depth(graph, start, destiny):
    for depth in range(len(graph.content)):
        path = ld.limited_depth_search(graph, start, destiny, depth)
        if path:
            print("Path found at DEPTH: ", depth)
            return path
    return None


def run(graph, origin, destiny, runner):
    if runner:
        print("\n\nIterative Depth Search:\n---------------------")
        path = iterative_depth(graph, origin, destiny)
        if path:
            return path
        else:
            print("No path found.")
            return None
