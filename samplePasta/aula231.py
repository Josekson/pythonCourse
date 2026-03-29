from abc import ABC, abstractmethod

class AbstractFoo(ABC):

    
    def __init__(self, name):
        self._name = None
        self.name = name
        

    @property
    @abstractmethod #esse operator deve vir sempre por ultimo 
    def name(self): ...
        
    #quando tiver um setter de uma property, o setter deve descer pra classe filha
'''    @name.setter
    def name(self,name):
        self._name = name '''

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        #print('Nao faz nada')
    
    @property #metodo para sobrepor o metodo abstrato da classe suprema 
    def name(self):
        return self._name
        
    #setter teve que descer pra classe filha, pq um setter so existe se tiver um property
    @name.setter
    def name(self,name):
        self._name = name 

foo = Foo('Bar')
print(foo.name)