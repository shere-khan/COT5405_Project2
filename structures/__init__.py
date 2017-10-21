from structures import graph
from structures import heap

if __name__ == '__main__':
    f = open('input/input2.txt', 'r')

    read_edges = False

    g = graph.Graph()
    vmap = {}
    edgelist = []
    emap = {}
    while True:
        c = f.read(1)
        if not c:
            print('End of file')
            break

        if c == '[':
            uid = f.read(1)
            u = None
            if uid not in vmap:
                u = graph.Vertex(uid, 'oo')
                g.insert_vertex_object(u)
                vmap[uid] = u
            else:
                u = vmap[uid]

        if c == ':':
            while c != '\n':
                c = f.read(1)
                if c == '(':
                    vid = f.read(1)
                    v = graph.Vertex(vid, 'oo')
                    if vid not in vmap:
                        g.insert_vertex_object(v)
                        vmap[vid] = v
                    else:
                        v = vmap[vid]
                    while c != '\n' and c != ',':
                        c = f.read(1)
                        if c == '|':
                            w = ''
                            c = f.read(1)
                            while c != ')':
                                w += c
                                c = f.read(1)
                            id1 = uid + vid
                            id2 = vid + uid
                            if id1 not in emap and id2 not in emap:
                                edgelist.append(graph.Edge(u, v, int(w)))
                                emap[id1] = True
    # list(map(lambda x: g.insert_edge_object(x), edgelist))

    for e in edgelist:
        g.insert_edge_object(e)

    mst = graph.GraphTool.mst(g)
    print(mst)
    path = graph.GraphTool.shortest_path(g, vmap['A'], vmap['E'])
    print(path)
