class Camera:
    def __init__(self,nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'A câmera {self.nome} já está filmando.')
            return 0
        print(f'{self.nome} agora a câmera está filmando.')
        self.filmando = True

    def parar_de_filmar(self):
        if not self.filmando:
            print(f'A câmera {self.nome} já não está filmando.')
            return 0
        self.filmando = False
        print(f'{self.nome} parou de filmar.')


    def fotografar(self):
        if self.filmando:
            print(f'A câmera {self.nome} não pode filmar e fotografar ao mesmo tempo.')
            return 0 
        print(f'Fotografado.')
        

c1 = Camera('Canon')
print(c1.filmando)
c1.filmar()
c1.fotografar()
c1.filmar()
c1.parar_de_filmar()
c1.parar_de_filmar()
c1.fotografar()
print('MUDANÇA DE CAMERA! AGORA!')

c2 = Camera('Sony')
print(c2.filmando)
c2.filmar()
c2.fotografar()
c2.filmar()
c2.parar_de_filmar()
c2.parar_de_filmar()
c2.fotografar()