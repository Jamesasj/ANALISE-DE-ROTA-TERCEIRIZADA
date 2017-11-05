from Restricao import Restricao
from Lotacao import Lotacao
from Pedidos import Pedidos
from Dijkistra import grafo

def criarDados():
    g = grafo()
    g = gerarGrafo(g)
    l = Lotacao()
    l.add_carro('1', 100)
    l.add_carro('2', 100)
    l = gerarLotacao(l)
    r = Restricao()
    r = gerarRestricao(r)
    p = Pedidos()
    p = gerarPedidos(p)
    return g,l,r,p

def gerarPedidos(p):
    p.add_pedido('14','7')
    p.add_pedido('19','2')
    p.add_pedido('20','2')
    p.add_pedido('22','5')
    p.add_pedido('15','7')
    p.add_pedido('23','9')
    p.add_pedido('16','3')
    p.add_pedido('16','6')
    p.add_pedido('16','5')
    p.add_pedido('16','5')
    p.add_pedido('21','5')
    p.add_pedido('18','6')
    p.add_pedido('18','7')
    p.add_pedido('17','3')
    return p

def gerarRestricao(r):
    r.add_produto_produto('3' , '6')
    r.add_produto_produto('10' , '3')
    r.add_produto_produto('10' , '6')
    return r

def gerarLotacao(l):
    l.add_lotacao('1','1',8.33)
    l.add_lotacao('1','2',2.5)
    l.add_lotacao('1','3',6.25)
    l.add_lotacao('1','4',2.5)
    l.add_lotacao('1','5',2.5)
    l.add_lotacao('1','6',5.26)
    l.add_lotacao('1','7',2.5)
    l.add_lotacao('1','8',5)
    l.add_lotacao('1','9',2.5)
    l.add_lotacao('1','10',16.6)

    l.add_lotacao('2','1',50)
    l.add_lotacao('2','2',10)
    l.add_lotacao('2','3',100)
    l.add_lotacao('2','4',10)
    l.add_lotacao('2','5',6.66)
    l.add_lotacao('2','6',25)
    l.add_lotacao('2','7',10)
    l.add_lotacao('2','8',25)
    l.add_lotacao('2','9',6.66)

    return l

def gerarGrafo(g):
    g.add_cliente('14')
    g.add_cliente('20')
    g.add_cliente('20')
    g.add_cliente('22')
    g.add_cliente('23')
    g.add_cliente('16')
    g.add_cliente('16')
    g.add_cliente('21')
    g.add_cliente('21')
    g.add_cliente('18')
    g.add_cliente('17')
    g.add_aresta('14','20',2786)
    g.add_aresta('14','18',1949)
    g.add_aresta('20','14',1617)
    g.add_aresta('20','21',2856)
    g.add_aresta('22','16',1262)
    g.add_aresta('23','21',2540)
    g.add_aresta('16','17',1651)
    g.add_aresta('16','22',1256)

    g.add_aresta('21','23',2540)
    g.add_aresta('18','14',1964)
    g.add_aresta('17','16',1515)
    g.add_aresta('19','21',4338)
    g.add_aresta('21','19',4682)
    g.add_aresta('17','15',4735)
    g.add_aresta('17','19',6868)

    g.add_aresta('20','21',2856)
    g.add_aresta('17','20',6437)

    return g