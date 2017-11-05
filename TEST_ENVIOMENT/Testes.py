from GeradorRotas import executar 
from RestricaoFactory import criarRestricao1
from LotacaoFactory import criarLotacoa1
from PedidosFactoy import criarPedidos1
from GrafoFactory import criarGrafo
from Restricao import Restricao
from Lotacao import Lotacao
from Pedidos import Pedidos
from Dijkistra import grafo
"""
Testes :
 - Feito        Dois produtos iguais para o mesmo cliente e um não cabe
 - Feito        Faltou um produto no cliente
 - Feito        Pois produtos para o mesmo cliente
 - Feito        Trocar Carro Lotado
 - Feito        Troca de Clientes
 - Feito        Termino por falta de carros
 - Feito        Restrições de Produtos por outros pordutos
 - Feito        Restrições de Produtos com carros
 - Feito        Restrições de lotação
 - Feito        Montagem de rota do dia 2
 - Feito        Acabaram os produtos
 - Feito        Rotas fora do caminho com mais intemediario?
 - Feito        Produtos fora da rota minima
 - Não Feito    Decisão de terceirizar
 - Não feito    Calcular custo de terceirizar a cada iteração
 - Não Feito    Formatar Resultados
"""
def main():
    cenario1()

def cenario1():
    grafo = criarGrafo()
    restricao_p_p = criarRestricao1()
    lotacao_c_p = criarLotacoa1()
    pedidos = criarPedidos1() 
    print('###################### Restrições de Produto #########################')
    print(restricao_p_p.mProd_prod)
    print('\n###################### Locação do Veiculo #########################')
    print(lotacao_c_p.lotacao)   
    print('\n###################### Pedidos #########################')
    print(pedidos.clientes)   
    executar(grafo, restricao_p_p, lotacao_c_p, pedidos)


if __name__ == '__main__':
    main()