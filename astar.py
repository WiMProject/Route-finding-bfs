from collections import defaultdict
from queue import PriorityQueue

heuristics = {
    "TPS UNAI": 629,
    "TPS Regol": 446,
    "TPS Tegallega": 421,
    "TPS Gedebage": 320,
    "TPS Antapani": 246,
    "TPS Pagarsih": 248,
    "TPS Pasar Ciwastra": 132,
    "TPS Sarimukti": 156,
    "TPS Jalan Ambon": 108,
    "TPA Babakan": 0
}

graph = defaultdict(list)

def astar_search(source, target, graph):
    open_set = PriorityQueue()
    open_set.put((heuristics[source], source))
    came_from = {}
    g_score = {node: float('inf') for node in heuristics}
    g_score[source] = 0

    while not open_set.empty():
        current_node = open_set.get()[1]

        if current_node == target:
            return reconstruct_path(came_from, current_node)

        for neighbor in graph[current_node]:
            tentative_g_score = g_score[current_node] + 1  # Assuming uniform cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristics[neighbor]
                open_set.put((f_score, neighbor))

    return []

def reconstruct_path(came_from, current_node):
    total_path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        total_path.append(current_node)
    return total_path[::-1]

def addedge(x, y):
    graph[x].append(y)
    graph[y].append(x)

# Menambahkan edges ke dalam graph
addedge("TPS UNAI", "TPS Regol")
addedge("TPS Regol", "TPS Tegallega")
addedge("TPS Regol", "TPS Gedebage")
addedge("TPS Tegallega", "TPS Antapani")
addedge("TPS Gedebage", "TPS Antapani")
addedge("TPS Gedebage", "TPS Pagarsih")
addedge("TPS Gedebage", "TPS Pasar Ciwastra")
addedge("TPS Gedebage", "TPS Sarimukti")
addedge("TPS Antapani", "TPS Pagarsih")
addedge("TPS Pagarsih", "TPS Pasar Ciwastra")
addedge("TPS Pasar Ciwastra", "TPS Sarimukti")
addedge("TPS Pasar Ciwastra", "TPA Babakan")
addedge("TPS Sarimukti", "TPA Babakan")
addedge("TPS Sarimukti", "TPS Jalan Ambon")
