from collections import deque
import heapq

###################################################
# Busca gulosa implementada: Dijkstra
# Teoricamente, Dijkstra eh igual a busca BFS porem
# com um calculo de custo de movimento.
####################################################

# A PriorityQueue do python eh mais custosa para uso.
# Usando essa estrategia de implementar uma nova
# PriorityQueue com heaps.
class GreedyPriorityQueue:

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

###################################################
# Implementacao simples do algoritmo de Dijkstra
###################################################
def greedy_dijkstra_search(graph, start, target):
    queue = GreedyPriorityQueue()
    queue.put(start, 0)
    path = {}
    cost = {}

    path[start] = None
    cost[start] = 0

    while not queue.empty():
        current = queue.get()

        if current == target:
            break

        for next in graph[current]:
            new_cost = cost[current] + 1 # custo unico
            if next not in cost or new_cost < cost[next]:
                cost[next] = new_cost
                priority = new_cost
                queue.put(next, priority)
                path[next] = current

    result = get_path(path, start, target)
    print("Caminho final:", result)
    return result
    #return get_path(path, start, target)
    #return path, cost

# retornando o caminho final
def get_path(result, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = result[current]
    path.append(start) 
    path.reverse() 
    return path
