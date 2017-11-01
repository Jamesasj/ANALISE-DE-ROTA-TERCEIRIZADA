from collections import defaultdict
class grafo:
    def __init__(self):
        self.lClientes = set()
        self.arestas = defaultdict(list)
        self.mDistancias = {}

    def add_cliente(self, value):
        self.lClientes.add(value)

    def add_aresta(self, origem, destino, distance):
        self.arestas[origem].append(destino)
        self.arestas[destino].append(origem)
        self.mDistancias[(origem, destino)] = distance


def dijsktra(grafo, initial):
    clientesVisitados = {initial: 0}
    rota = {}

    lClientes = set(grafo.lClientes)

    while lClientes: 
        min_cliente = None
        for cliente in lClientes:
            if cliente in clientesVisitados:
                if min_cliente is None:
                    min_cliente = cliente
                elif clientesVisitados[cliente] < clientesVisitados[min_cliente]:
                    min_cliente = cliente

        if min_cliente is None:
            break

        lClientes.remove(min_cliente)
        custo_atual = clientesVisitados[min_cliente]

        for aresta in grafo.arestas[min_cliente]:
            aux = grafo.mDistancias[(min_cliente, aresta)]  if ((min_cliente, aresta) in grafo.mDistancias) else 0
            custo = custo_atual + aux
            if aresta not in clientesVisitados or custo < clientesVisitados[aresta]:
                clientesVisitados[aresta] = custo
                rota[aresta] = min_cliente

    return clientesVisitados, rota