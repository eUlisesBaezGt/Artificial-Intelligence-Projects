def greedy_best_first_search(graph, origin, destination, h):
    """
    Function that performs a search in a graph using the Greedy
    best-first search algorithm with a given heuristic.
    """
    tree = {}
    priority_queue = [(origin, 0, [])]

    while priority_queue:
        node, _ , path = priority_queue.pop(0)
        if node == destination:
            # If the goal node is reached, return the path
            return path + [node]
        
        if node not in tree:
            # If the node is not in the tree, add it
            tree[node] = []
            
            # Generate the successors of the current node
            successors = [(node_s[0], h[node_s[0]]) for node_s in graph.content[node]]
            
            # Sort the successors by their heuristic value
            successors.sort(key=lambda x: x[1])

            # Add the successors to the priority queue
            for node_s , _ in successors:
                priority_queue.append((node_s, h[node_s], path + [node]))
    
    # If the goal node is not reached, return None
    return None