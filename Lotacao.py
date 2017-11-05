from collections import defaultdict
class Lotacao():
    def __init__(self):
        self.lotacao = {}
        self.carros = dict()
        self.carrosCopia = dict()
        self.index = -1
        self.lProdutos = defaultdict(list)
        self.lRota = defaultdict(list)
        self.lCustos = {}
        self.lCustosRota = []
        self.lDias = []
    
    def add_carro(self, carro, max_lotacao):
        self.carros[carro] = max_lotacao
        self.carrosCopia[carro] = max_lotacao

    def add_lotacao(self, carro, produto, ocupacao):
        self.lotacao[(carro, produto)] = ocupacao 
    
    def proximoCarro(self):
        if not (self.carros) :
            self.carro = None
            return None
        else:
            self.carro = self.carros.popitem()
            return self.carro[0]

    def pegarProdutos(self):
        return self.lProdutos[self.carro[0]]

    def existeLotacao(self, produto):
        if ((self.carro[0], produto) in self.lotacao):
            return True
        return False

    def existeEspaco(self, produto):
        ocupacao = self.lotacao[(self.carro[0], produto)]
        capacidade = self.carro[1]
        return ocupacao <= capacidade

    def colocarProdutoCarro(self, produto, cliente, custo):
        self.lRota[self.carro[0]].append({cliente:produto})
        
        self.lCustos[(self.carro[0], cliente)] = custo

        ocupacao = self.lotacao[(self.carro[0], produto)]
        capacidade = self.carro[1]
        novaCapacidade = capacidade - ocupacao
        
        self.carro = (self.carro[0], novaCapacidade)
        self.lProdutos[self.carro[0]].append(produto)

    def carroEstaCheio(self):
        capacidade = self.carro[1]
        return capacidade == 0

    def reiniciarCarros(self):
        for carro in self.carrosCopia:
            self.carros[carro] = self.carrosCopia[carro]
        self.lDias.append(self.lRota)
        self.lCustosRota.append(self.lCustos)
        self.lCustos = {}
        self.lRota = defaultdict(list)
        self.lProdutos = defaultdict(list)

    def adicionarCusto(self, cliente, custo):
        self.lCustos[(self.carro[0], cliente)] = custo
        