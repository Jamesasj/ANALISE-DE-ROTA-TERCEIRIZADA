from Lotacao import Lotacao

def criarLotacoa1():
    l = Lotacao()
    l.add_carro('1001', 100)
    l.add_carro('1002', 100)

    l.add_lotacao('1001','101',40)
    l.add_lotacao('1001','102',1)
    l.add_lotacao('1001','103',10)
    l.add_lotacao('1001','104',10)
    l.add_lotacao('1001','105',10)
   # l.add_lotacao('1001','106',10) #carro 1 não levra produtos 106 
    l.add_lotacao('1001','107',10)
    l.add_lotacao('1001','108',10)
    l.add_lotacao('1001','109',10)

    l.add_lotacao('1002','101',9)
    l.add_lotacao('1002','102',1)
    l.add_lotacao('1002','103',1)
    l.add_lotacao('1002','104',9)
    l.add_lotacao('1002','105',1)
    l.add_lotacao('1002','106',6)
    l.add_lotacao('1002','107',1)
    l.add_lotacao('1002','108',1)
    l.add_lotacao('1002','109',1)

    return l