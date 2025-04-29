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
def calcula_pontos_full_house(lrolados):
    dicio= {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    l=[]
    soma=0
    for dado in lrolados:
        if dado in dicio.keys():
            dicio[dado] += 1
        if dicio[dado] >= 2 and dado not in l:
            l.append(dado)
    if len(l) != 2:
        return 0
    if dicio[l[0]] == 2 and dicio[l[1]] != 3:
        return 0
    if dicio[l[0]] == 3 and dicio[l[1]] != 2:
        return 0
    for dado in l:
        soma += dado * dicio[dado]
    return soma
def calcula_pontos_quadra(lista):
    dicio = {}
    soma = 0
    for dado in lista:
        if dado not in dicio:
            dicio[dado] = 1
        else:
            dicio[dado] += 1
        if dicio[dado] == 4:
            for i in range(len(lista)):
                soma += lista[i]
            break
    return soma
def calcula_pontos_quina(lista):
    dicio = {}
    soma = 0
    for dado in lista:
        if dado not in dicio:
            dicio[dado] = 1
        else:
            dicio[dado] += 1
        if dicio[dado] == 5:
            for i in range(len(lista)):
                soma = 50
            break
    return soma
def calcula_pontos_regra_avancada(lista):
    d = {}
    p1 = calcula_pontos_quina(lista)
    p2 = calcula_pontos_full_house(lista)
    p3 = calcula_pontos_quadra(lista)
    p4 = calcula_pontos_soma(lista)
    p5 = calcula_pontos_sequencia_alta(lista)
    p6 = calcula_pontos_sequencia_baixa(lista)
    d['cinco_iguais'] = p1
    d['full_house'] = p2
    d['quadra'] = p3
    d['sem_combinacao'] = p4
    d['sequencia_alta'] = p5
    d['sequencia_baixa'] = p6
    return d
def faz_jogada(lista,cat,cartela):
    psimples = calcula_pontos_regra_simples(lista)
    pavançado = calcula_pontos_regra_avancada(lista)
    if cat not in ['1', '2', '3', '4', '5', '6']:
        cartela['regra_avancada'][cat] = pavançado[cat]
    else:
        categoria = int(cat)
        cartela['regra_simples'][categoria] = psimples[categoria]
    return cartela
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)