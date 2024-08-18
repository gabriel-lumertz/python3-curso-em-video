# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# numero = int(input('Digite um número inteiro: '))

# if(numero % 2 != 0 and numero / numero == 1):
#     print(numero % 2)
#     print(numero / numero)
#     print('O número {} é primo.'.format(numero))
# else:
#     print(numero % 2)
#     print(numero / numero)
#     print('O número {} não é primo.'.format(numero))


numero = int(input('Digite um número: '))
total = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print("\033[31m", end='')
    print('{} '.format(i), end='')


print('\n\033[mO núemro {} foi divisível {} vezes.'.format(numero, total))

if(total == 2):
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')