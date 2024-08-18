# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número inteiro: '))

if(numero % 2 != 0 and numero / numero == 1):
    print(numero % 2)
    print(numero / numero)
    print('O número {} é primo.'.format(numero))
else:
    print(numero % 2)
    print(numero / numero)
    print('O número {} não é primo.'.format(numero))