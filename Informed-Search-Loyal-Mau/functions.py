def show_path(path):
    if path:
        print("PATH FOUND:")
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i])
            else:
                print(path[i], end=" -> ")


def show_path_dijkstra(path, weight):
    if path:
        print("PATH FOUND:")
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i])
            else:
                print(path[i], end=" -> ")

        print("TOTAL WEIGHT: ", weight)


def nodes_list(graph):
    nodes = []
    for node in graph.content:
        if node not in nodes:
            nodes.append(node.upper())
    return nodes


def check_origin(graph, origin):
    nodes = nodes_list(graph)
    if origin.upper() not in nodes:
        print("Origin not found.")
        return False
    return True


def check_destiny(graph, destiny):
    nodes = nodes_list(graph)
    if destiny.upper() not in nodes:
        print("Destiny not found.")
        return False
    return True
