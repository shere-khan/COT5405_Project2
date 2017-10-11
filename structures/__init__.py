from structures import graph

if __name__ == '__main__':
    g = graph.Graph()
    graph.GraphTool.create_connected_graph(g, 5, 1, 3, 5, 0.3)
