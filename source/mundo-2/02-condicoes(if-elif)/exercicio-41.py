# A confedaração nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# 14 anos: INFANTIL
# 19 anos: JUNIOR
# 25 anos: SÉNIOR
# Acima: MASTER

from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Qual o ano de nascimento do atelta: '))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print('O atleta tem {} anos e é da categoria Mirim.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e é da categoria infantil.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e é da categoria Júnior.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e é da categoria Sênior.'.format(idade))
else:
    print('O atleta tem {} anos e é da categoria Master.'.format(idade))