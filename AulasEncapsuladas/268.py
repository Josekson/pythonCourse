from dataclasses import dataclass,asdict,astuple,field

@dataclass(repr=True)
class Pessoa:
    nome:str = 'Missing'
    sobrenome:str = 'Not sent'
    idade: int = 1000


if __name__ == '__main__':

    p1 = Pessoa()

    print(asdict(p1).keys(),type(asdict(p1)))
    print(asdict(p1).values(),type(asdict(p1)))
    print(asdict(p1).items(),type(asdict(p1)))
    print(astuple(p1),type(astuple(p1)))
    print(f'\n{p1}')
