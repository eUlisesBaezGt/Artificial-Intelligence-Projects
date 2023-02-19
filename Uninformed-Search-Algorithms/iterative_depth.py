def iterative_depth(graph, start, goal):
    for depth in range(len(graph.content)):
        path = depth_limited_search(graph, start, goal, depth)
        if path:
            print("Path found at depth: ", depth)
            return path
    return None


def depth_limited_search(graph, origin, destiny, limit):
    if origin == destiny:
        return [origin]
    if limit == 0:
        return None
    for node in graph.content[origin]:
        path = depth_limited_search(graph, node[0], destiny, limit - 1)
        if path:
            return [origin] + path
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
