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
# Implementacao simples baseada no
# algoritmo de Dijkstra
###################################################
def uniform_cost_search(graph, start, target):
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
    #print("Caminho final:", result)
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


######################################################
# Busca em largura BFS (funcionando)
######################################################
def breadth_first_graph_search(graph, start, target):
    queue = deque([[start]])
    seen = set([start])
    
    while queue:
        # get the first path from the queue
        path = queue.popleft()
        # get the last node from the path
        node = path[-1]
        # path found
        if node == target:
            print("Caminho final:",path)
            return path
        else:
            print("Testando:", path)
            
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        #for adjacent in graph.get(node, []):
        for adjacent in graph[node]:
            if adjacent not in seen:
                seen.add(adjacent)
                # mantendo registro
                #queue.append(list(path).append(adjacent))
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                
                
###########################################
# Busca em profundidade (funcionando)
# Depth First Search
###########################################
def depth_first_search(graph, start, end):
    queue = deque([[start]])

    seen = set([start])

    while queue:
        # mudando aqui
        path = queue.pop()
    
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            print("Achou:", path)
            return path
        else:
            print("Testando:", path)

        # enumerate all adjacent nodes, construct a new path and push it into the queue
        #for adjacent in graph.get(node, []):
        for adjacent in graph[node]:
            if adjacent not in seen:
                seen.add(adjacent)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
