class Multiplicador:
    def __init__(self, fator):
        self.fator = fator

    def __call__(self,x):
        return 'nada'

m2 = Multiplicador(2)

print(callable(m2))   # True
print(m2(10))         # 20
