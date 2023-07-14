genero= str(input('digite o seu sexo')).strip().upper()[0]
while genero not in 'mMfF':
   genero = str(input('dados Inválidos! Mais uma vez digite seu sexo')).strip().upper()[0]
print('Obrigado!! genero regitrado com sucesso!')
