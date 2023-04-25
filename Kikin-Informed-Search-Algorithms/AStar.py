from queue import PriorityQueue

from KAGraph import KAGraph as KAg

# inicializar la función AStartSearch que recibe el grafo, la heuristica, el punto de orign  y el destino


def AStarSearch(graph, heuristics, origin="Arad", destination="Bucharest"):
    # inicializa la variable frontier con PriorityQueue()
    frontier = PriorityQueue()
    # agrega el origne a frontier
    frontier.put(origin, 0)
    # inicializamos un diccionario vacío
    came_from = {}
    # inicaliza el diccionario cost_so_far con el valor origin que tiene la llave 0
    cost_so_far = {origin: 0}
    # ciclo que se repite hasta que frontier no esté vacío
    while not frontier.empty():
        # toma el valor actual de la frontera
        current = frontier.get()
        # si el valor actual es igual al destino, la busqueda termina
        if current == destination:
            break
        # itera dentro de todos los nodos
        for next_node in graph.get_neighbors(current):
            # new_cost recive el valor del nodo actual
            new_cost = cost_so_far[current] + \
                int(graph.get_weight(current, next_node))
            # is el noso no setá en en cost_so_far o el costo es menor al del siguiente...
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                # el siguiente nodo toma el valor new_cost
                cost_so_far[next_node] = new_cost
                # la variable priority va a sumar new_cost con la heuristica del nodo siguiente
                priority = new_cost + \
                    int(heuristics.get_weight(next_node, destination))
                # agrega el valor next_node y prority a frontier
                frontier.put(next_node, priority)
                # da el valor de next_node en el diccionaroi con el valor current
                came_from[next_node] = current

    # Reconstruct the path
    path = [destination]

    while path[-1] != origin:
        # agrega el último valor del path de came_fomr
        path.append(came_from[path[-1]])
    # voltea el path
    path.reverse()
    # imprime el costo
    print(f"Cost: {cost_so_far[destination]}")
    # regresa el valor de path
    return path


def main():
    # inicializa el grafo
    graph = KAg.Graph()
    # abre el file graph.txt
    with open("graph.txt") as file:
        lines = file.readlines()
    # itera cada una de las líenas
    for i in range(1, len(lines)):
        # separa las lineas en 3 valores: origen, destino y peso
        origin, destination, weight = lines[i].split()
        # agrega los datos al grafo
        graph.add_edge(origin, destination, weight)

    # inicializa el grafo para la heuristica
    heuristics = KAg.Graph()
    with open("heuristics.txt") as file:
        lines = file.readlines()
    # itera cada una de las lineas
    for i in range(1, len(lines)):
        # separa las lineas en 3 valores: origen, destino y peso
        origin, destination, weight = lines[i].split()
        #  agrega los datos al grafo
        heuristics.add_edge(origin, destination, weight)

    # genera el camino desde la función AStarSearch que recibe los dos grafos.
    path = AStarSearch(graph, heuristics)
    # imprime el grafo
    print(f"Path: {path}")


if __name__ == "__main__":
    main()
