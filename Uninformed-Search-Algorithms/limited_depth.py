def limited_depth_search(graph, origin, destiny, limit):
    if origin == destiny:
        return [origin]
    if limit == 0:
        return None
    for node in graph.content[origin]:
        path = limited_depth_search(graph, node[0], destiny, limit - 1)
        if path:
            return [origin] + path
    return None


def run(graph, origin, destiny, runner):
    print("\n\nLimited Depth Search:\n---------------------")
    limit = int(input("Limit: "))
    if runner:
        path = limited_depth_search(graph, origin, destiny, limit)
        return path

    # ASK: IF GIVEN LIMIT
