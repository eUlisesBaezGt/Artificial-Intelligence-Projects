def show_path(path):
    if path:
        print("PATH FOUND:")
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i])
            else:
                print(path[i], end=" -> ")
    else:
        print("PATH NOT FOUND")
