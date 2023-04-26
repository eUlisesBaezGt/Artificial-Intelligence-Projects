# This function prints the given path.
def show_path(path):
    # Check if the path exists.
    if path:
        # If the path exists, print the path in the required format.
        print("PATH FOUND:")
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i])
            else:
                print(path[i], end=" -> ")
    # If the path doesn't exist, print an error message.
    else:
        print("PATH NOT FOUND")
