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
def calcula_pontos_sequencia_baixa(lrolados):
    soma=0
    l=[]
    for dado in lrolados:
        if dado not in l:
            l.append(dado)
    l=sorted(l)
    for i in range(len(l)-3):
        if len(l) < 4:
            return soma
        if l[i] == l[i+1] - 1 and l[i+1] == l[i+2] - 1 and l[i+2] == l[i+3] - 1:
            soma = 15
    return soma
def calcula_pontos_sequencia_alta(lrolados):
    l=[]
    for dado in lrolados:
        if dado not in l:
            l.append(dado)
    l=sorted(l)
    if len(l) < 5:
            return 0  
    for i in range(len(l)-1):
        if l[i+1] != l[i] + 1:
            return 0
    return 30