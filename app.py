from flask import Flask, render_template, request
import networkx as nx
import matplotlib.pyplot as plt
from greedy import greedy_search, graph as greedy_graph, heuristics
from astar import astar_search, graph as astar_graph, heuristics

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    route = None
    if request.method == 'POST':
        algorithm = request.form['algorithm']
        source_number = int(request.form['source'])
        target_number = int(request.form['target'])
        node_list = list(heuristics.keys())  # Assuming both graphs have the same nodes
        source = node_list[source_number - 1]
        target = node_list[target_number - 1]

        if algorithm == 'greedy':
            route = greedy_search(source, target, greedy_graph)
            graph = greedy_graph
        elif algorithm == 'astar':
            route = astar_search(source, target, astar_graph)
            graph = astar_graph

        # Visualisasi graf menggunakan NetworkX dan Matplotlib
        plot_graph(graph, route, source, target)

    return render_template('index.html', route=" -> ".join(route) if route else None)

def plot_graph(graph, route, source, target):
    G = nx.Graph()

    # Menambahkan node ke dalam graf
    for node in heuristics:
        G.add_node(node)

    # Menambahkan edges ke dalam graf
    for key, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(key, neighbor)

    # Menentukan posisi node dalam graf
    pos = nx.spring_layout(G)

    # Menggambar node dan edges
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2)

    # Menambahkan label ke node
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

    # Menyoroti jalur yang diikuti
    path_edges = list(zip(route, route[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=8, alpha=0.5, edge_color='r')

    # Menyoroti node awal dan akhir
    nx.draw_networkx_nodes(G, pos, nodelist=[source], node_size=700, node_color='g')
    nx.draw_networkx_nodes(G, pos, nodelist=[target], node_size=700, node_color='b')

    # Menyimpan graf
    plt.title("Visualisasi Graf dan Hasil Pencarian")
    plt.savefig('static/graph.png')
    plt.clf()  # Membersihkan plot untuk penggunaan berikutnya

if __name__ == '__main__':
    app.run(debug=True)
