class MeuError(Exception):
    ...

def levantar():
    exception_ = MeuError('a','b','c')
    raise exception_

try:
    #1/0
    levantar()
except (MeuError,ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    raise