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

def roda_jogo(cartela,dados,guardados):
    c = 0
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    ação = (input('>'))
    while ação != '0':
        if ação == '1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            ind = int(input('>'))
            lista = guardar_dado(dados,guardados,ind)
            dados = lista[0]
            guardados = lista[1]
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            ação = input(('>'))
        elif ação == '2':
            print('Digite o índice do dado a ser removido (0 a 4):')
            ind = int(input('>'))
            lista = remover_dado(dados,guardados,ind)
            dados = lista[0]
            guardados = lista[1]
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            ação = input(('>'))
        elif ação == '3':
            if c == 2:
                print('Você já usou todas as rerrolagens.')
            else:
                dados = rolar_dados(len(dados))
                c+=1
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            ação = input(('>'))
        elif ação == '4':
            imprime_cartela(cartela)
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            ação = input(('>'))
        else:
            print("Opção inválida. Tente novamente.")
            ação = (input('>'))  
    dadosfinais = dados + guardados
    regra = 0
    print('Digite a combinação desejada:')
    combinação = (input('>'))
    numeros = ['1','2','3','4','5','6']
    while True:
        if combinação in numeros:
            cat = int(combinação)
        else:
            cat = combinação

        if (cat in cartela['regra_simples'] and cartela['regra_simples'][cat] != -1) \
        or (cat in cartela['regra_avancada'] and cartela['regra_avancada'][cat] != -1):
            print("Essa combinação já foi utilizada.")
            combinação = input('> ')
        elif cat not in cartela['regra_simples'] and cat not in cartela['regra_avancada']:
            print("Combinação inválida. Tente novamente.")
            combinação = input('> ')
        else:
            break
    faz_jogada(dadosfinais, combinação, cartela)
    return cartela
c=0
imprime_cartela(cartela)
print(f'Dados rolados: {dados}')
print(f'Dados guardados: {guardados}')
while c < 12:
    cartela = roda_jogo(cartela, dados, guardados)
    dados = rolar_dados(5)
    guardados = []
    if c != 11:
        print(f'Dados rolados: {dados}')
        print(f'Dados guardados: {guardados}')
    c += 1
soma = 0
total = 0
for combinacao,valores in cartela.items():
    for pontos in valores.values():
        total+=pontos
        if combinacao == 'regra_simples':
            soma += pontos
if soma>=63:
    total += 35

imprime_cartela(cartela)
print(f'Pontuação total: {total}')