import breadth
import depth
import dijkstra
import iterative_depth
import limited_depth
import two_way

runProgram = True
while runProgram:
    print("Welcome to the path finding program!")
    print("Please select the algorithm you would like to use:")
    print("1. Breadth First Search")
    print("2. Depth First Search")
    print("3. Dijkstra's Algorithm")
    print("4. Iterative Deepening Depth First Search")
    print("5. Limited Depth First Search")
    print("6. Two Way Search")
    print("7. Exit")
    choice = input("Please enter your choice: ")
    if choice == "1":
        breadth.run()
    elif choice == "2":
        depth.run()
    elif choice == "3":
        dijkstra.run()
    elif choice == "4":
        iterative_depth.run()
    elif choice == "5":
        limited_depth.run()
    elif choice == "6":
        two_way.run()
    elif choice == "7":
        runProgram = False
    else:
        print("Invalid choice. Please try again.")
