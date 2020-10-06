def inicio(frase):
    escolha = int(input(f'''{frase}
\n1 - para jogar uma partida isolada
2 - para jogar um campeonato '''))
    return escolha


def computador_escolhe_jogada(n, m):
    computador = m
    while True:
        if (n - computador) % (m+1) == 0:
            break
        else:
            computador -= 1
    print(f'''\nO computador tirou {computador} peça(s).
Agora restam {n-computador} peça(s) no tabuleiro.''')
    return computador


def usuario_escolhe_jogada(n, m):
    humano = m + 1
    while humano > m or humano < 1:
        humano = int(input(f'\nQuantas peças você vai tirar? '))
        if humano > m or humano < 1:
            print('\nOops! Jogada inválida! Tente de novo.')
    print(f'''\nVocê tirou {humano} peça(s).
Agora restam {n-humano} peça(s) no tabuleiro.''')
    return humano


def partida():
    n = int(input('\nQuantas peças: '))
    m = int(input('Limite de peças por jogada: '))
    while m > n or m < 1:
        print('\nOops! Jogada inválida! Tente de novo.')
        m = int(input('Limite de peças por jogada: '))
    if n % (m + 1) == 0:
        print('\nVocê começa!')
        humano = usuario_escolhe_jogada(n, m)
        n -= humano
    else:
        print('\nComputador começa!')
    while n > 0:
        computador = computador_escolhe_jogada(n, m)
        n -= computador
        if n <= 0:
            break
        humano = usuario_escolhe_jogada(n, m)
        n -= humano
    print('Fim do jogo! O computador ganhou!')


def campeonato():
    for ciclo in range(1, 4):
        print(f"\n{'*' * 4} Rodada {ciclo} {'*' * 4}")
        partida()
    print(f"\n{'*' * 4} Final do campeonato! {'*' * 4}")
    print(f"\nPlacar: Você 0 X 3 Computador")


escolha = inicio('Bem-vindo ao jogo do NIM! Escolha:')
while escolha != 1 and escolha != 2:
    escolha = inicio('\nOpção inválida! Escolha:')
if escolha == 1:
    print('\nVocê escolheu uma partida isolada!')
    partida()
if escolha == 2:
    print('\nVoce escolheu um campeonato!')
    campeonato()
