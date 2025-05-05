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


while rodada<12:
    imprime_cartela(cartela)
    print(f'Dados rolados: {dados}')
    print(f'Dados guardados: {guardados}')
    c = 0
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    ação = int(input('>'))
    while ação != 0:
        if ação == 1:
            print('Digite o índice do dado a ser guardado (0 a 4):')
            ind = int(input('>'))
            while ind > 4 or ind < 0:
                print('Opção inválida. Tente novamente.')
                print('Digite o índice do dado a ser guardado (0 a 4):')
                ind = int(input('>'))
            lista = guardar_dado(dados,guardados,ind)
            dados = lista[0]
            guardados = lista[1]
        if ação == 2:
            print('Digite o índice do dado a ser removido (0 a 4):')
            ind = int(input('>'))
            while ind > 4 or ind < 0:
                print('Opção inválida. Tente novamente.')
                print('Digite o índice do dado a ser removido (0 a 4):')
                ind = int(input('>'))
            lista = remover_dado(dados,guardados,ind)
            dados = lista[0]
            guardados = lista[1]
        if ação == 3:
            if c >= 3:
                print('Você já usou todas as rerrolagens.')
                print(f'Dados rolados: {dados}')
                print(f'Dados guardados: {guardados}')
                print(('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:'))
                ação = int(input('>'))
            numero = 5-len(guardados)
            dados = rolar_dados(numero)
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
            c+=1
        if ação == 4:
            imprime_cartela(cartela)
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
        ação = int(input('>'))
    print('Digite a combinação desejada:')
    i = input('>')
    fazer a parte de colocar tudo na cartela
    rodada +=1