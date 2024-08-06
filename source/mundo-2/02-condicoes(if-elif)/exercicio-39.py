# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ainda vai se alistar ao sarviço militar.
# Se é a hora da sa alistar.
# Se já passou do tempo do alistamanto.

# Seu programa também davará mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input('Qual o seu ano de nascimento? '))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

# print(idade)

if idade < 18:
    print('Você ainda vai se alistar. Faltam {} anos'.format(18 - idade))
elif idade > 18:
    print('Já passou do tempo de se alistar. Passou {} anos'.format(idade - 18))
else:
    print('Está na hora de se alistar.')