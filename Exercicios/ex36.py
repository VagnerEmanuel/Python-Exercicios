casa = float(input('Qual o valor da casa?'))
salário = float(input('Qual a sua renda?'))
anos = int(input('Quantos anos de finaciamento?'))
prestação = casa / (anos * 12)
minimo= salário * 30/100
print('Para financiar uma casa de {:.2f} R$, em {} anos'.format(casa, anos))
print('O valor da  prestação será de {:.2f} R$'.format(prestação))
if prestação <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

