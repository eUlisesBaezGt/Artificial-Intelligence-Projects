from Graph import *
import breadth
# import depth
# import dijkstra
# import iterative_depth
import limited_depth

# import two_way

runProgram = True


def main():
    global runProgram

    graph = Graph()
    with open("data.txt") as file:
        lines = file.readlines()

    for i in range(1, len(lines)):
        origin, destiny, weight = lines[i].split()
        graph.new_edge(origin, destiny, weight)

    print("Welcome to the path finding program!")
    while runProgram:
        print("\n\nMAIN MENU\n")
        print("Please select the algorithm you would like to use:")
        print("1. Breadth First Search")
        print("2. Depth First Search")
        print("3. Dijkstra's Algorithm")
        print("4. Iterative Deepening Depth First Search")
        print("5. Limited Depth First Search")
        print("6. Two Way Search")
        print("7. Exit")
        print("--------------------")
        choice = input("Please enter your choice: ")
        if choice == "1":
            breadth.run(graph)
        elif choice == "2":
            # depth.run(graph)
            pass
        elif choice == "3":
            # dijkstra.run(graph)
            pass
        elif choice == "4":
            # iterative_depth.run(graph)
            pass
        elif choice == "5":
            limited_depth.run(graph)
        elif choice == "6":
            # two_way.run(graph)
            pass
        elif choice == "7":
            runProgram = False
            print("\nFINISHED\n")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
