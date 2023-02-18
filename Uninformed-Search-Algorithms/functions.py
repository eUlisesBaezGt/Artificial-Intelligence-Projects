def show_path(path, origin, destiny):
    print("\n\nRESULTS:\n--------")
    print("FROM:", origin)
    print("TO:", destiny)
    print("\nPATH FOUND:")
    if path:
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i])
            else:
                print(path[i], end=" -> ")
    else:
        print("No path found")


def check_origin(graph, origin):
    if origin not in graph.content:
        print("Origin not found.")
        return False
    return True


def check_destiny(graph, destiny):
    if destiny not in graph.content:
        print("Destiny not found.")
        return False
    return True
