class Foo:
    def __init__(self):
        self.public = 'Isso é publico' #pode ser usado em tudo
        self._protected = 'Isso é protegido' #pode ser usado em sua classe e subclasses, mas nao deve ser usado fora da sua classe ou das suas subclasses
        self.__private = 'Isso é privado'#Só deve ser usado na classe em que foi declarado
        
    
    def metodo_publico(self):
        return 'metodo publico'

    def _metodo_protegido(self):
        return 'metodo protegido'
    
    def __metodo_privado(self):
        return 'metodo privado'

f = Foo()

print(f.public)
print(f._protected)

print(f.__metodo_privado())
print(f.metodo_publico())
print(f._metodo_protegido())