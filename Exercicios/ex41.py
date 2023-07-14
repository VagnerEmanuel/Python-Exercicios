from datetime import date
ano = int(input('Qual o seu ano de nascimento?'))
atual = date.today().year
idade = atual - ano
print ('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Você é um atleta mirim')
elif idade > 9 and idade <= 14:
    print('Voce é um atleta infantil')
elif idade > 14 and idade <=19:
    print('Você é um atleta Junior')
elif idade > 19 and idade <= 25:
    print('Você é um atleta Senior')
else:
    print('Você é um atleta master')