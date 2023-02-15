import functions as f


def limited_depth_search(graph, origin, destiny, limit=9):
    if origin == destiny:
        return [origin]
    if limit == 0:
        return None
    for node in graph.content[origin]:
        path = limited_depth_search(graph, node[0], destiny, limit - 1)
        if path:
            return [origin] + path
    return None


def run(graph):
    print("\n\nLimited Depth Search:\n---------------------")
    print("Origin: ", end="")
    origin = input()
    print("Destiny: ", end="")
    destiny = input()
    path = limited_depth_search(graph, origin, destiny)
    f.show_path(path, origin, destiny)
