import functions as f


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


def run(graph):
    runner = True
    print("\n\nBreadth First Search:\n---------------------")
    print("Origin: ", end="")
    origin = input().title()
    runner = f.check_origin(graph, origin)
    print("Destiny: ", end="")
    destiny = input().title()
    runner = f.check_destiny(graph, destiny)
    if runner:
        path = breadth_first_search(graph, origin, destiny)
        f.show_path(path, origin, destiny)
