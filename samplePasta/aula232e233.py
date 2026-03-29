from abc import ABC,abstractmethod



class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self)-> bool:
        ...

class NotificacaoEmail(Notificacao):
    
    def enviar(self)-> bool:
        print('E-mail: enviando -',self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    
    def enviar(self)-> bool:
        print('SMS: enviando -',self.mensagem)
        return False

def notificar(notificacao: Notificacao): #estou dizendo que notificaçao é do tipo string
    notificacao_enviada = notificacao.enviar()#notificaçao é do tipo notificaçao
    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NAO enviada')
    

notificar(NotificacaoEmail('testando e-mail'))

notificacao_sms = NotificacaoSMS('Testando sms')
notificar(notificacao_sms)