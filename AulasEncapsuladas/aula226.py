class Ponto:
    def __init__(self,x,y,z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'(x={self.x},y={self.y})'

    def __repr__(self): #repr irá mostrar minha classe e os meus atributos quando eu printar um objeto
        #return self.__class__.__name__
        return f'{self.__class__.__name__}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
        #colocar o "!r" no final de cada atributo para que ele print o type correto do atributo

p1 = Ponto(1,2)
p2 = Ponto(999,888)
print(repr(p1))
print(p2)