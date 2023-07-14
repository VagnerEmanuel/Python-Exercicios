nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
media =(nota1 + nota2)/ 2
print('suas notas foram {} e {}. Sua média é {}'.format(nota1, nota2, media))
if media >= 5 and media < 7:
    print('Você está de recuperação!')
elif media < 5:
    print('Você foi reprovado')
else:
    print('parabéns você foi aprovado')
