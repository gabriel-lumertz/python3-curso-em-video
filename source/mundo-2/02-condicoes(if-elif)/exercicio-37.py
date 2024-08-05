# Escrava um programa que leia um número inteiro qualquer a peça para o usuário escolhar qual sará a base de conversão:

# 1 para binário
# 2 para octal
# 3 para haxadacimal

numero = int(input('Escolha um número inteiro: '))

tipo = int(
        input(
            'Como gostaria de converter?\n'
            '1 - Binário?\n'
            '2 - Octadeximal?\n'
            '3 - Hexadecimal?\n'
        )
    )

if tipo == 1:
    print(f'{numero} convertido para binário é {bin(numero)[2:]}')
elif tipo == 2:
    print(f'{numero} convertido para binário é {oct(numero)[2:]}')
elif tipo == 3:
    print(f'{numero} convertido para binário é {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente.')