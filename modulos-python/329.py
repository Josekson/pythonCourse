from threading import Thread

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade):
        if  self.estoque < quantidade:
            print(f'NÃO TEMOS INGRESSO(S) SUFICIENTE')
            return
        
        print(f'VOCÊ COMPROU {quantidade} INGRESSO(S)')
        self.estoque = self.estoque - quantidade
        print(f'AINDA TEMOS {self.estoque}')
        

if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1,20):
        t = Thread(target=ingressos.comprar,args=(i,))
        t.start()
        print(ingressos.estoque)