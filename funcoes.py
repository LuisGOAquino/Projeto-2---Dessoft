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
def remover_dado(rolados,estoque,remover):
    rolados.append(estoque[remover])
    del(estoque[remover])
    return[rolados,estoque]
def calcula_pontos_regra_simples(lrolados):
    dicio= {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in lrolados:
        dicio[dado]+=dado
    return dicio
def calcula_pontos_soma(lrolados):
    soma=0
    for dado in lrolados:
        soma+=dado
    return soma
        