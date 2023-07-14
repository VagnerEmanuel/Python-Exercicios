#validação de dados
s = str(input('informe seu sexo [M\F]:')).strip().upper()[0]
while s not in 'mMfF':
    s= str(input('Dados inválidos. Digite novamente seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(s))