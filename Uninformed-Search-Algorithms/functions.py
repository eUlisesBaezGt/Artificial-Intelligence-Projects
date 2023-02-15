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
