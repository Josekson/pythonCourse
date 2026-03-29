class A:
    pass

    def quem_sou(self):
        print('A')

class B(A):
    pass

'''    def quem_sou(self):
        print('B')'''

class C(A):
    pass

    def quem_sou(self):
        print('C')

class D(B,C):
    pass

    '''def quem_sou(self):
        print('D')'''

d = D()
d.quem_sou()