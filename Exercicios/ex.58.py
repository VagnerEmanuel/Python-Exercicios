from random import randint
computador = randint(0, 10)
print('Sou o deu computador...')
print('Acabei de pensar em um número entre 0 e 10' )
print('Será que você consegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    Jogador = int(input('Qual o seu palpite?'))
    palpite += 1
    if Jogador == computador:
        acertou = True
        print('Acertou com {} palpites'.format(palpite))
    else:
        if Jogador < computador:
            print('Mais.... Tente outra vez!')
        elif Jogador >computador:
            print('Menos... tente outra vez!')

