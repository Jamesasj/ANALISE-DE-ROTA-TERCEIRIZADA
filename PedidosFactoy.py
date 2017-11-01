from Pedidos import Pedidos
def criarPedidos1():
    p = Pedidos()
    p.add_pedido('2','101')
    p.add_pedido('2','101')
    p.add_pedido('3','101')
    p.add_pedido('4','101')
    p.add_pedido('7','101')

    p.add_pedido('6','107')
    p.add_pedido('6','106')

    p.add_pedido('5','101')
    p.add_pedido('5','101')
    p.add_pedido('5','102')
    p.add_pedido('5','105')
    return p
