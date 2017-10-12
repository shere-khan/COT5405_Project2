from structures import graph
from structures import heap

if __name__ == '__main__':
    g = graph.Graph()
    graph.GraphTool.create_connected_graph(g, 5, 1, 3, 5, 0.1)
    print(graph.GraphTool.is_connected(g))
    graph.GraphTool.print_graph_matrix_sequentially(g)

    t = heap.HeapPriorityQueue()

