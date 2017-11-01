class Restricao():
    def __init__(self):
        self.mProd_prod = {}
        
    def add_produto_produto(self, produto1, produto2):
        self.mProd_prod[(produto1, produto2)] = 1
        self.mProd_prod[(produto2, produto1)] = 1

    def existeRestricao(self, produto, lProduto):
        for produto2 in lProduto:
            if (produto,produto2) in self.mProd_prod:
                return True
        return False

        