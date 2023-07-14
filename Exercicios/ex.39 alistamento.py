from datetime import date
atual = date.today().year
ano = int(input('digite seu ano de nascimento'))
idade = atual - ano
print('quem nasceu em {} tem {} anos em {}'.format(ano,idade, atual))
if idade < 18:
    resto = 18 - idade
    print('você tem {} anos ainda faltam {} anos para você se alistar'.format(idade, resto))
    resto2 = atual + resto
    print('você tem que se alistar no ano de {}'.format(resto2))
elif idade == 18:
    print('Esse é o seu ano de alistamento, corra para uma junta militar')
else:
    resto = idade - 18
    print(' você ja passou do seu ano de alistamento')
    resto2 = atual - resto
    print('você deveria ter se alistado no ano de {}'.format(resto2))