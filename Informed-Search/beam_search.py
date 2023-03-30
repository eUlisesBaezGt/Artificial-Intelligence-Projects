#Este código se puede utilizar usando heaps (colas de prioridad) para optimizar el uso en memoria
# y el tiempo de ejecución.
# 
# Este programa al ordenar la lista en cada iteración tiene una complejidad de tiempo de: O(n*log(n))
# Al usar Heap, la complejidad es de: O(log(n)) 


def beam_search(graph, start, goal, heuristic_table, beam_width):
    visited = set()
    queue = [(0, [start])]  # (cost, path)

    while queue:
        current_paths = []

        # Obtener las 'beam_width' rutas con el menor costo en la cola
        sorted_queue = sorted(queue, key=lambda x: x[0])
        selected_paths = sorted_queue[:beam_width]

        for cost, path in selected_paths:
            queue.remove((cost, path))
            current_node = path[-1]

            if current_node == goal:
                return path

            if current_node not in visited:
                visited.add(current_node)
                for neighbor, edge_cost in graph.content[current_node]:
                    total_cost = cost + int(edge_cost) + int(heuristic_table[neighbor])
                    current_paths.append((total_cost, path + [neighbor]))

        queue.extend(current_paths)

    return None