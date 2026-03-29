from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
        if novo_nome == 'ABRAAO':
            raise ValueError('Não aceito nome Abraão')
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,nova_idade):
        if nova_idade == 99:
            raise ValueError('Não aceito essa idade')
        self._idade = nova_idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta #agregacao de conta corrente ou poupança

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        self.cont_valor_limite_atual = 0
    
    def deposito(self,valor):
        tipo_de_conta = self.whoami()
        self.saldo = self.saldo + valor
        return f'Você depositou R$ {valor:.2f}\nSua conta é {tipo_de_conta} e seu saldo é de R$ {self.saldo:.2f}.'

    def sacar_base(self, valor):
        tipo_de_conta = self.whoami()
        valor_do_limite = self.valor_limite()
        
        if isinstance(valor,float):
            return 'Só é possível sacar valores inteiros.'
        if valor>self.saldo:
            return f'Você não possui saldo suficiente.'
        if  self.cont_valor_limite_atual >= valor_do_limite:
            return f'Sua conta é {tipo_de_conta} e você atingiu o limite de saque.'
        self.saldo = self.saldo - valor
        self.cont_valor_limite_atual+=1
        self.valor_limite_atual = valor_do_limite - self.cont_valor_limite_atual
        return f'Sua conta é {tipo_de_conta} e você ainda possui {self.valor_limite_atual} saque(s). Seu saldo é de R$ {self.saldo:.2f}.'


    @abstractmethod
    def valor_limite(self): ...

    @abstractmethod
    def whoami(self):...

class ContaCorrente(Conta):

    def whoami(self):
        return 'corrente'

    def valor_limite(self):
        return 5

class ContaPoupanca(Conta):

    def whoami(self):
        return 'poupança'

    def valor_limite(self):
        return 3
   
class Banco:
    def __init__(self,*cliente_conta):
        self.cliente_conta = cliente_conta

    def autenticar(self,cliente,conta)-> bool:
        for cliente_banco,conta_banco in self.cliente_conta:
            if cliente_banco is cliente and conta_banco is conta:
                return True
        return False

conta_corrente_josekson = ContaCorrente(2239,1111,750)
conta_poupanca_yasmin = ContaPoupanca(9322,2222,1050)
conta_corrente_poliana = ContaCorrente(4221,1000,350)
conta_poupanca_fernanda = ContaPoupanca(4221,5000,5000)

cliente_josekson = Cliente('Josekson',27,conta_corrente_josekson)
cliente_yasmin = Cliente('Yasmin',28,conta_poupanca_yasmin)
cliente_poliana = Cliente('Poliana',30,conta_corrente_poliana)
cliente_fernanda = Cliente('Fernanda',23,conta_poupanca_fernanda)


banco1 = Banco((cliente_josekson, conta_corrente_josekson),
               (cliente_yasmin, conta_poupanca_yasmin),
               )

banco2 = Banco((cliente_poliana, conta_corrente_poliana),
               (cliente_fernanda, conta_poupanca_fernanda),
               )

def sacar(cliente_:Cliente, conta_:Conta, banco:Banco, valor:int):
    eh_autentico = banco.autenticar(cliente_,conta_)
    if eh_autentico:
        print('Sua conta é autência e o saque foi permitido:')
        return cliente_.conta.sacar_base(valor)
    return 'Conta não é autêntica para saque!'


if __name__=='__main__':
    print(banco1.autenticar(cliente_josekson, conta_corrente_josekson))
    print(banco1.autenticar(cliente_josekson, conta_corrente_poliana))

    print(sacar(cliente_josekson, conta_corrente_josekson,banco1,30))
    print(sacar(cliente_josekson, conta_corrente_josekson,banco1,30))
    print(sacar(cliente_josekson, conta_corrente_josekson,banco1,30))
    print(sacar(cliente_josekson, conta_corrente_josekson,banco1,30))
    print(sacar(cliente_josekson, conta_corrente_josekson,banco1,30))
    print(sacar(cliente_josekson, conta_corrente_josekson,banco1,30))
    print(sacar(cliente_josekson, conta_corrente_josekson,banco1,30))