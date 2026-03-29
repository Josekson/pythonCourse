class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        # O super("a classe filha que deseja que ele procure o método no pai", self)
        retorno = super().upper() #super() é usado quando desejo executar algo antes e/ou depois da função
        print('ACABOU O UPPER')
        return retorno

string = MinhaString('Luiz')
#print(string.upper())

class A:
    atributo_a = 'AAAA'

    def __init__(self,atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):

    # atributo_a virá para classe B pois ela está herdando tudo de A
    atributo_b = 'BBBB' # variavel criado em B
    
    def __init__(self,atributo,outra_coisa):
        super().__init__(atributo) #atributo do A
        self.outra_coisa = outra_coisa # atributo do B

    def metodo(self): # Este método vai sobrepor o metodo de criado A, pois ambos tem mesmo nome
        print('B')

class C(B):
    #atributo_a e atributo_b  vêm para cá pois C herda tudo de B e B possui atributo_a
    atributo_c = 'CCCC'

    def __init__(self, *arg, **kwargs): #Toda vez que chama a classe, o init é executado
        super().__init__(*arg, **kwargs)
        print('Ei, burlei o sistema')

    def metodo(self):# Este método vai sobrepor todos os outros metodos
        super(C,self).metodo() #Vai executar o método Pai do C
        super(B,self).metodo() #Vai executar o método Pai do B
        print('C')

c = C('Lucas','Dante')
'''print(c.atributo,c.outra_coisa)
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)

c.metodo()'''