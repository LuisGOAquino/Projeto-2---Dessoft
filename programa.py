from funcoes import *

rodada = 0

cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

dados = rolar_dados(5)
guardados = []
imprime_cartela(cartela)

while rodada<12:
    print(f'Dados rolados: {dados}')
    print(f'Dados guardados: {guardados}')
    c = 0
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    ação = (input('>'))
    while ação != '0':
        if ação == '1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            ind = int(input('>'))
            while ind > len(dados) - 1 or ind < 0:
                print('Opção inválida. Tente novamente.')
                print('Digite o índice do dado a ser guardado (0 a 4):')
                ind = int(input('>'))
            lista = guardar_dado(dados,guardados,ind)
            dados = lista[0]
            guardados = lista[1]
        while guardados == [] and ação == '2':
            print('Opção inválida. Tente novamente.')
            ação=(input('>'))  
        if ação == '2':
            print('Digite o índice do dado a ser removido (0 a 4):')
            ind = int(input('>'))
            while ind > len(guardados) - 1 or ind < 0:
                print('Opção inválida. Tente novamente.')
                print('Digite o índice do dado a ser removido (0 a 4):')
                ind = int(input('>'))
            lista = remover_dado(dados,guardados,ind)
            dados = lista[0]
            guardados = lista[1]
        if ação == '3':
            if c == 1:
                print('Você já usou todas as rerrolagens.')
            else:
                numero = 5-len(guardados)
                dados = rolar_dados(numero)
                c+=1
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
            print(('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:'))
            ação = (input('>'))
        if ação == '4':
            imprime_cartela(cartela)
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
        while ação not in ['0','1','2','3','4']:
            print('Opção inválida. Tente novamente.')
            ação = (input('>'))
        if ação == 0:
            break
        print(f'Dados rolados: {dados}')
        print(f'Dados guardados: {guardados}')      
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
        ação = (input('>'))
    dadosfinais = dados + guardados
    confirmação = False
    regra = None
    print('Digite a combinação desejada:')
    combinação = int(input('>'))
    while combinação not in ['1','2','3','4','5','6','sem_combinacao','quadra','full_house','sequencia_baixa','sequencia_alta','cinco_iguais']:
        print('Combinação inválida. Tente novamente.')
        print('Digite a combinação desejada:')
        combinação = int(input('>'))
    if combinação in cartela['regra_simples']:
        confirmação = True
        regra = 'regra_simples'
    if combinação in cartela['regra_avancada']:
        confirmação = True
        regra = 'regra_avancada'
    else:
        cartela = faz_jogada(dadosfinais,combinação,cartela)
    c = 0
    dados = rolar_dados(5)
    guardados = []
    rodada += 1

    
soma = 0
total = 0
for valor in cartela['regra_simples'].values():
    somas += valor
    total += valor

for valor in cartela['regra_avancada'].values():
    total += valor

if soma>=63:
    total += 35

imprime_cartela(cartela)
print(f'Pontuação total: {total}')