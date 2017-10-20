from structures import graph
from structures import heap

if __name__ == '__main__':
    f = open('input/input.txt', 'r')

    read_edges = False

    g = graph.Graph()
    g.outgoing()
    vmap = {}
    edgelist = []
    while True:
        c = f.read(1)
        if not c:
            print('End of file')
            break

        if c == '[':
            vid = f.read(1)
            u = graph.Vertex(vid, 'oo')
            g.insert_vertex_object(u)
            vmap[vid] = u

        if c == ':':
            while c != '\n':
                c = f.read(1)
                if c == '(':
                    vid = f.read(1)
                    v = graph.Vertex(vid, 'oo')
                if c == '|':
                    w = ''
                    c = f.read(1)
                    while c != ')':
                        w += c
                        c = f.read(1)
                    edgelist.append(graph.Edge(u, v, int(w)))

    # list(map(lambda x: g.insert_edge_object(x), edgelist))

    for e in edgelist:
        g.insert_edge_object(e)

    mst = graph.GraphTool.mst(g)
    path = graph.GraphTool.shortest_path(vmap['A'], vmap['E'])
    print(path)
