peso = float(input('Qual o seu peso (Kg)'))
altura = float(input('Qual a sua altura (m)'))
imc = peso / (altura ** 2)
print('seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('você está na faixa de sobrepeso')
elif 30 <= imc < 40:
    print('Você está na faixa de obesidade')
else:
    print('Obesidade mórbida')