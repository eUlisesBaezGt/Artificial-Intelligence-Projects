def a_star(graph, origin, destination, ht):
     # Create a dictionary to store the cost of each node visited
    costs = {origin: 0}
    # Create a dictionary to store the path to each node visited
    paths = {origin: []}
    # Create a list to store the nodes to visit
    frontier = [origin]

    while frontier:
        # Sort the nodes to visit by their f score
        frontier.sort(key=lambda node: costs[node] + int(ht[node]))
        # Get the node with the lowest f score
        current = frontier.pop(0)
    
        if current == destination:
            # If the goal node is reached, return the optimal path
            return paths[current] + [current]
        
        # Generate the successors of the current node
        for next_node, _ in graph.content[current]:
        # Calculate the cost to reach the next node
            for i in graph.content[current]:
                if i[0] == next_node:
                    cost = costs[current] + int(i[1])
                if next_node not in costs or cost < costs[next_node]:
                # If the next node has not been visited yet, or if the
                # cost to reach it is lower than the previous cost, update
                # the cost and path, and add it to the frontier
                    costs[next_node] = cost
                    paths[next_node] = paths[current] + [current]
                    if next_node not in frontier:
                        frontier.append(next_node)
    # If the goal node is not reached, return None
    return None
        