from random import *
def rolar_dados(n):
    l=[]
    for i in range(n):
        sorteado= randint(1,6)
        l.append(sorteado)
    return l
def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado=dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado)
    del(dados_rolados[dado_para_guardar])
    return [dados_rolados, dados_no_estoque]