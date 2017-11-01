from collections import defaultdict
class Pedidos():
    def __init__ (self):
        self.clientes = defaultdict(list)
    
    def add_pedido(self, cliente, produto):
        self.clientes[cliente].append(produto)

    def avaliarClientesSemPodutos(self):
        semProduto = []
        for cliente in self.clientes:
            produtos = self.clientes[cliente]
            if not produtos:
                semProduto.append(cliente)
        return semProduto