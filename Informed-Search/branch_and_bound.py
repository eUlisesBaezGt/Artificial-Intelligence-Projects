def branch_and_bound(graph, origin, destination, ht):
    """
    Function that performs a search in a graph using the Branch and Bound
    algorithm with a given heuristic, and returns the optimal path from the
    start node to the goal node.
    """
    # Initialize the frontier with the start node and its heuristic value
    frontier = [(float(ht[origin]), [origin])]
    # Initialize the best path and its cost as infinity
    best_path = None
    best_cost = float('inf')
    
    while frontier:
        # Sort the paths in the frontier by their lower bound cost
        frontier.sort(key=lambda x: x[0])
        # Get the path with the lowest lower bound cost
        (cost, path) = frontier.pop(0)
        # Get the last node in the path
        node = path[-1]
        
        if node == destination:
            # If the goal node is reached, update the best path and its cost
            if cost < best_cost:
                best_path = path
                best_cost = cost
        else:
            # Generate the successors of the current node
            for next_node, _ in graph.content[node]:
                # If the next node has not been visited yet, calculate its
                # lower bound cost and add it to the frontier
                if next_node not in path:
                    next_cost = cost + float(ht[next_node])
                    next_path = path + [next_node]
                    frontier.append((next_cost, next_path))
    
    return best_path