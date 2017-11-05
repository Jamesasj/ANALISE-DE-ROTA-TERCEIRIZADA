from Dijkistra import grafo
def criarGrafo():
    g = grafo()
    g.add_cliente('1')
    g.add_cliente('2')
    g.add_cliente('3')
    g.add_cliente('4')
    g.add_cliente('5')
    g.add_cliente('6')
    g.add_cliente('7')

    g.add_aresta('1','2',2)
    g.add_aresta('1','3',4)
    g.add_aresta('1','4',5)
    g.add_aresta('2','4',2)
    g.add_aresta('3','4',1)
    g.add_aresta('3','7',4)
    g.add_aresta('4','6',2)
    g.add_aresta('4','7',3)
    g.add_aresta('6','5',5)
    g.add_aresta('6','7',1)
    g.add_aresta('7','5',7)
    return g
