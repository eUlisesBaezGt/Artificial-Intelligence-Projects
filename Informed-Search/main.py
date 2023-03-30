from Graph import *
#import breadth
import greedy_best_first
import string
from beam_search import beam_search
import functions as f
import branch_and_bound

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

print("GREEDY_BEST_FIRST SEARCH")
#path = greedy_best_first.greedy_best_first_search(graph, origin, "Bucharest", ht)
#print(path)
print("-----------------")
print("A* SEARCH")
#path = a_star.a_star(graph, origin, "Bucharest", ht)
#print(path)
print("-----------------")
print("WEIGHTED A* SEARCH")
#w = float(input("Enter factor W: "))
#path = weighted_a_star.weighted_a_star(graph, origin, "Bucharest", ht, w)
#print(path)
print("-----------------")
print("BRANCH AND BOUND")
path = branch_and_bound.branch_and_bound(graph, origin, "Bucharest", ht)
print(path)

print("BEAM SEARCH:")
beam_width = 3  # Ajusta este valor según tus necesidades
beam_path = beam_search(graph, origin, "Bucharest", ht, beam_width)
print(beam_path)
print("-----------------")