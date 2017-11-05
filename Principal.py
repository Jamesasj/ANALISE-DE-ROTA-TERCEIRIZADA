from GeradorRotas import executar 
from realFactoy import criarDados
from Restricao import Restricao
from Lotacao import Lotacao
from Pedidos import Pedidos
from Dijkistra import grafo

def main():
    grafo, lotacao_c_p, restricao_p_p, pedidos = criarDados()
 
    print('###################### Restrições de Produto #########################')
    print(restricao_p_p.mProd_prod)
    print('\n###################### Locação do Veiculo #########################')
    print(lotacao_c_p.lotacao)   
    print('\n###################### Pedidos #########################')
    print(pedidos.clientes)   
    executar(grafo, restricao_p_p, lotacao_c_p, pedidos)

if __name__ == '__main__':
    main()