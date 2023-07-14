num1 = int(input('primeiro valor'))
num2 = int(input('segundo valor'))
opção =0
while opção != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] novos números')
    print('[5] Sair do programa')
    opção = int(input('Qual a sua opção?'))
    if opção == 1:
        soma= num1 + num2
        print('A soma entra {} e {} é {}'.format(num1, num2, soma))
print('FIM')
