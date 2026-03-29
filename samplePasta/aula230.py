#é necessario importar abc para criar classes abstratas
#classes abstratas é toda classe que herda de ABC e possui ao menos um método abstrato
from abc import ABC, abstractmethod


class Log(ABC): #uma classe abstrata quando não quero que ela seja executada
                #eu quero que outras classes herdem dela

    @abstractmethod #isso faz com que o método abaixo seja abstrato
    def log(self,msg): ...
    
    def log_error(self,msg):
        return self.log(f'Error: {msg}')   

    def log_success(self,msg):
        return self.log(f'Success: {msg}')
    
class LogPrintMixin(Log):
    def log(self,msg): #é necessario criar uma classe para sobrepor a classe abstrata
      print(f'{msg} -> {self.__class__.__name__}')
 

l = LogPrintMixin()
l.log_error('OI')