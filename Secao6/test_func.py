def teste():
    var1 = True
    var2 = False
    var3 = 'teste3'
    var4 = 'teste4'
    var5 = 'teste5'
    return var1,var2,var3,var4,var5 

def teste2():
    global var,var1
    if var1==True:
        print('peguei da teste')
    var = False
    print(var)

_,_,x,*_ = teste()

print(x)