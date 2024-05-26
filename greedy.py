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

def greedy_search(source, target, graph):
    visited = {}
    route = []

    for key in heuristics:
        visited[key] = False

    visited[source] = True
    p_queue = PriorityQueue()
    p_queue.put((heuristics[source], source))

    while not p_queue.empty():
        current_node = p_queue.get()[1]
        route.append(current_node)

        if current_node == target:
            break

        for node in graph[current_node]:
            if not visited[node]:
                visited[node] = True
                p_queue.put((heuristics[node], node))

    return route

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
