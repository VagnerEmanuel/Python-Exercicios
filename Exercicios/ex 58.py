from random import randint
computador = randint (0, 10)
print ('sou seu computador! Acabei de pensar em um numero de 0 10 ')
print ('será que você consegue acertar?')
Jogador= int(input('Qual é o seu palpite?'))
while Jogador != computador:
    if Jogador < computador:
        Jogador = int(input(('digite um número maior')))
    elif Jogador > computador:
        Jogador = int(input(('digite um número menor')))
else:
    print('parabén você acertou')
