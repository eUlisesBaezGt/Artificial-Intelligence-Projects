from Graph import *
import breadth
import greedy_best_first
import string
import functions as f

graph = Graph()

filename = "weighted_test.txt"
heur = "heuristic.txt"

ht = dict()
with open(heur) as h:
      lines = h.readlines()
      for i in lines:
            node, heuristic = i.split()
            ht[node] = heuristic


with open(filename) as file:
      lines = file.readlines()
      for i in range(1,len(lines)):
            origin, destination, weight = lines[i].split()
            graph.new_edge(origin, destination, weight)
            graph.new_edge(destination, origin, weight)

print("Origin: ", end="")
origin = input()
origin = string.capwords(origin).translate({ord(c): None for c in string.whitespace})
origin2 = origin.translate({ord(c): None for c in string.whitespace})
runner1 = f.check_origin(graph, origin2)

print("The destination is Bucharest.")

# print("Destination: ", end="")
# destiny = input()
# destiny = string.capwords(destiny).translate({ord(c): None for c in string.whitespace})
# destiny2 = destiny.translate({ord(c): None for c in string.whitespace})
# runner2 = f.check_destiny(graph, destiny2)

#runner = runner1 and runner2
print("GREEDY_BEST_FIRST SEARCH:")
path = greedy_best_first.greedy_best_first_search(graph, origin, "Bucharest", ht)
print(path)
print("-----------------")
print(graph.content)