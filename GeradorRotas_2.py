from Dijkistra import dijsktra
from Dijkistra import grafo
from Restricao import Restricao
from Lotacao import Lotacao
from Pedidos import Pedidos
from GuardarResultados import DAO

def executar(grafo, restricao, lotacao, pedidos):
    origem = '17'
    print('\n###################### Inicio da Execução ########################')
    custos, rota = dijsktra(grafo, origem)
    print('\n###################### Rotas calculadas ########################')
    print(rota)
    print('\n###################### custos calculadas ########################')
    print(custos)

    lIntermediarios = calcularNosIntermedirios(rota, origem)
    
    while lIntermediarios:
        lIntermediarios = criarRotas(lotacao, pedidos, restricao, origem, rota, custos, lIntermediarios)
    
def criarRotas(lotacao, pedidos, restricao, origem, rota, custos, lIntermediarios):
    max_cliente = buscar_max_cliente(lIntermediarios,custos)
    

def buscar_max_cliente(lIntermediarios, lCusto):
    max_intemediario = None
    for no in lIntermediarios:
        if max_intemediario is None:
            max_intemediario = no
        elif lIntermediarios[no] > lIntermediarios[max_intemediario]:
            max_intemediario = no
        elif lIntermediarios[no] == lIntermediarios[max_intemediario]:
            max_intemediario = no if lCusto[no] > lCusto[max_intemediario] else  max_intemediario
    return max_intemediario

def preencherCarro(carro, cliente, produto , restricao, lotacao)
    if (not restricao.existeRestricao(produto, lotacao.pegarProdutos(carro))):
        if(lotacao.existeLotacao(produto)):
            if(lotacao.existeEspaco( produto)):
                lotacao.colocarProdutoCarro(produto, cliente, custos[cliente])
                return True
    return False

def organizarResulta(lotacao):
    dao = DAO()
    dao.abrirEntregas()
    print('\n######################### Produtos entregues na rota ###################################')
    for dia, rotas in enumerate(lotacao.lDias):
        for carro in rotas:
            for lcliente in rotas[carro]:
                for cliente in lcliente:
                    print("Dia: {}, Carro: {}, cliente: {}, produto: {} ".format(str(dia), carro, cliente, lcliente[cliente]))
                    dao.guardar ([str(dia), carro, cliente, lcliente[cliente]])

    dao.fecharArquivo()

    dao.abrirRotas()
    print('\n######################### Custos das entregas ###################################')
    for dia, rotas in enumerate(lotacao.lCustosRota):
        for carroCliente in rotas:
            custo = rotas[carroCliente]
            print("Dia : {} , Carro : {} ,Cliente : {}, Custo : {}".format(dia, carroCliente[0], carroCliente[1], custo))
            dao.guardar([dia, carroCliente[0], carroCliente[1], custo])

    dao.fecharArquivo()