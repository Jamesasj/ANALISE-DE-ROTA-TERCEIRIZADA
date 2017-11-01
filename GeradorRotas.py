from Dijkistra import dijsktra
from Dijkistra import grafo
from Restricao import Restricao
from Lotacao import Lotacao
from Pedidos import Pedidos

def executar(grafo, restricao, lotacao, pedidos):
    origem = '1'
    print('\n###################### Inicio da Execução ########################')
    custos, rota = dijsktra(grafo, origem)
    qtdIntemerdiarias = calcularNosIntermedirios(rota)
    n = 1
    while qtdIntemerdiarias:
        print ('\n######################### Dia {} ######################'.format(n) )
        print("\n############### Quantidade de vizihos encontrados ###################")
        print(qtdIntemerdiarias)
        
        max_cliente = buscar_max_cliente(qtdIntemerdiarias, custos)
        pedidos, lotacao = preecherCarro(origem, max_cliente, pedidos, lotacao,restricao, rota, custos, qtdIntemerdiarias)
        
        lotacao.reiniciarCarros()
        n = n+1
    print('######################### Fim da Execução ###################################')

def removerIntermediriosSemProdutos(clientesSemProdutos, qtdIntemerdiarias):
    for cliente in clientesSemProdutos:
        if cliente in qtdIntemerdiarias:
            del qtdIntemerdiarias[cliente]
    return qtdIntemerdiarias

def preecherCarro(origem, max_cliente, pedidos, lotacao, restricao, rota, custos, qtdIntemerdiarias):
    print("\n############### Preenchendo os Carros ###################")
    cliente = max_cliente
    produtosCliente = pedidos.clientes[max_cliente]
    carro = lotacao.proximoCarro()
    lClientes = pedidos.clientes

    while lClientes:
        
        print('Cliente : {}, PrdotosClinete : {}, carro : {}'.format(cliente, produtosCliente, carro))
        
        clientesAtendidos, lotacao = incluirprodutos(cliente, lotacao, restricao, produtosCliente)
        
        if(clientesAtendidos):
            produtosCliente = removerClientes(produtosCliente, clientesAtendidos)
        
        clientesSemProdutos = pedidos.avaliarClientesSemPodutos()
        qtdIntemerdiarias = removerIntermediriosSemProdutos(clientesSemProdutos, qtdIntemerdiarias)
        max_cliente = buscar_max_cliente(qtdIntemerdiarias, custos)

        carro, cliente, produtosCliente, pararExecusao = avaliarPróximoPasso(origem, cliente, lotacao, carro, max_cliente, produtosCliente, pedidos, rota)
    
        if(pararExecusao):
            break
    print(lotacao.lRota)
    return pedidos, lotacao

def incluirprodutos(cliente, lotacao, restricao, produtosCliente):
    clientesAtendidos = []
    for indice, produto in enumerate(produtosCliente):
        if (not restricao.existeRestricao(produto, lotacao.pegarProdutos())):
            if(lotacao.existeLotacao(produto)):
                if(lotacao.existeEspaco( produto)):
                    lotacao.colocarProdutoCarro(produto, cliente)
                    clientesAtendidos.append(indice)
    return clientesAtendidos, lotacao

def removerClientes(produtosCliente, clientesAtendidos):
    clientesAtendidos.reverse()
    for indice in clientesAtendidos:
        del produtosCliente[indice]
    return produtosCliente

def calcularNosIntermedirios(rota):
    qtdIntemerdiarias = dict()
    for no in rota:
        proxNo = no
        count = 0
        while proxNo != '1':
            count += 1
            proxNo = rota[proxNo]
        qtdIntemerdiarias[no] = count
    return qtdIntemerdiarias

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

def avaliarPróximoPasso(origem, cliente, lotacao, carro, max_cliente, produtosCliente, pedidos, rota):
    pararExecucao = False
    if (lotacao.carroEstaCheio()):
        carro = lotacao.proximoCarro()
        cliente = max_cliente # reiniciar do primeiro cliente
        produtosCliente = pedidos.clientes[cliente]  
        if carro is None: # A rota do dia já usou todos os carros. armazenar todas dos carro e reiniciar no proximo cliente com pedidos
            carro = lotacao.reiniciarCarros()
    else:
        cliente = rota[cliente] #O carro não esta cheio e produtos não cabem então pega o prox cliente     
        if (cliente == origem):
            carro = lotacao.proximoCarro()
            cliente = max_cliente # reiniciar do primeiro cliente
            produtosCliente = pedidos.clientes[cliente]   
            if carro is None:
                pararExecucao = True
        else:
            produtosCliente = pedidos.clientes[cliente] 

    while not produtosCliente:
        if cliente is None:
            pararExecucao = True
            break
        cliente = rota[cliente] #pega o proximo cliente da rota     
        if (cliente == origem):
            carro = lotacao.proximoCarro()
            if carro is None:
                break
            else:
                cliente = max_cliente # reiniciar do primeiro cliente
                produtosCliente = pedidos.clientes[cliente]
        else:
            produtosCliente = pedidos.clientes[cliente]

    if (cliente == origem):
        pararExecucao = True 
    return carro, cliente, produtosCliente, pararExecucao