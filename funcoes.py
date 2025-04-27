from random import *
def rolar_dados(n):
    l=[]
    for i in range(n):
        sorteado= randint(1,6)
        l.append(sorteado)
    return l
