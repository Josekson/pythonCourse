from log import LogFileMixin



class Eletronico:
    def __init__(self,nome):
        self.nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado:
            self._ligado = False
    
class Smartphone(Eletronico,LogFileMixin):
    def ligar(self):
        super(Smartphone,self).ligar()
        if self._ligado:
            self.log_success(f'Você logou {self.nome}')

    def desligar(self):
        super(Smartphone,self).desligar()
        if not self._ligado:
            self.log_error(f'Você deslogou {self.nome}')
