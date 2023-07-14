num= int(input('digite um número'))
print('''Escolha uma das opções abaixo:
      [1] para binário
      [2] para Octal
      [3] para hexadecimal ''')
opção= int(input('Digite sua opção'))
if opção == 1:
      print('{} convertido para binário é {}'.format(num, bin(num)))
elif opção== 2:
      print('{} convertido para octal é {}'.format(num, oct(num)))
elif opção == 3:
      print('{} convertifo para hexadecimal é {}'.format(num, hex(num)))
else:
      print('Opção inválida! Tente de novo.')
