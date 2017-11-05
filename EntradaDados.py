from Restricao import Restricao
from Lotacao import Lotacao
from Pedidos import Pedidos
from Dijkistra import grafo
import csv

contexto = 'c:\\Users\\James\\Google Drive\\01 - FAESA\\2017.2\\06 - INTERDICIPLINAR\\BASE_DADOS\\'
GRAFO_FILE = contexto+'grafo.csv'
CLIENTES_FILE = contexto+'cliente.csv'
LOCATACAO_FILE = contexto+'lotacao.csv'
PEDIDOS_FILE = contexto+'pedidos.csv'
RESTRICOS_FILE = contexto+'restricao.csv'
CARROS_FILE = contexto + 'carros.csv'
def criarDados():
    g = grafo()
    g = gerarGrafo(g)
    l = Lotacao()
    l = gerarLotacao(l)
    r = Restricao()
    r = gerarRestricao(r)
    p = Pedidos()
    p = gerarPedidos(p)
    return g,l,r,p

def gerarPedidos(p):
    f = open(PEDIDOS_FILE, 'r')
    reader = csv.reader(f)
    for row in reader:
         p.add_pedido(row[0],row[1])
    f.close()
    return p

def gerarRestricao(r):
    f = open(RESTRICOS_FILE, 'r')
    reader = csv.reader(f)
    for row in reader:
         r.add_produto_produto(row[0],row[1])
    f.close()
    return r

def gerarLotacao(l):
    f = open(CARROS_FILE, 'r')
    reader = csv.reader(f)
    for row in reader:
          l.add_carro(row[0],int(row[1]))
    f.close()

    f = open(LOCATACAO_FILE, 'r')
    reader = csv.reader(f)
    for row in reader:
         l.add_lotacao(row[0],row[1],float(row[2]))
    f.close()
    return l

def gerarGrafo(g):
    f = open(CLIENTES_FILE, 'r')
    reader = csv.reader(f)
    for row in reader:
        g.add_cliente(row[0])
    f.close()

    f = open(GRAFO_FILE, 'r')
    reader = csv.reader(f)
    for row in reader:
        g.add_aresta(row[0],row[1],int(row[2]))
    f.close()
    return g